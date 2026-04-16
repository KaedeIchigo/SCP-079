from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from scp079.renderer import TerminalRenderer


VALID_OPERATORS = {
    "==",
    "!=",
    ">",
    "<",
    ">=",
    "<=",
    "in",
    "not_in",
    "contains",
    "contains_all",
}


@dataclass
class EngineSnapshot:
    current_node_id: str
    state: dict[str, Any]
    history: list[str] = field(default_factory=list)


class StoryEngine:
    def __init__(
        self,
        story_nodes: list[dict[str, Any]],
        start_node: str,
        default_state: dict[str, Any],
        renderer: TerminalRenderer | None = None,
    ) -> None:
        self.story_nodes = story_nodes
        self.node_map: dict[str, dict[str, Any]] = {n["id"]: n for n in story_nodes}
        self.start_node = start_node
        self.default_state = default_state
        self.renderer = renderer or TerminalRenderer()
        self.snapshot = EngineSnapshot(
            current_node_id=start_node,
            state=dict(default_state),
            history=[start_node],
        )

    def reset(self) -> None:
        self.snapshot = EngineSnapshot(
            current_node_id=self.start_node,
            state=dict(self.default_state),
            history=[self.start_node],
        )

    def save(self, path: str | Path) -> None:
        data = {
            "current_node_id": self.snapshot.current_node_id,
            "state": self.snapshot.state,
            "history": self.snapshot.history,
        }
        Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")

    def load(self, path: str | Path) -> None:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        self.snapshot = EngineSnapshot(
            current_node_id=data["current_node_id"],
            state=data["state"],
            history=data.get("history", [data["current_node_id"]]),
        )

    @staticmethod
    def _compare(left: Any, operator: str, right: Any) -> bool:
        if operator == "==":
            return left == right
        if operator == "!=":
            return left != right
        if operator == ">":
            return left > right
        if operator == "<":
            return left < right
        if operator == ">=":
            return left >= right
        if operator == "<=":
            return left <= right
        if operator == "in":
            return left in right
        if operator == "not_in":
            return left not in right
        if operator == "contains":
            return right in left
        if operator == "contains_all":
            return all(item in left for item in right)
        raise ValueError(f"Invalid operator: {operator}")

    def conditions_met(self, conditions: list[dict[str, Any]] | None) -> bool:
        if not conditions:
            return True
        for condition in conditions:
            key = condition["key"]
            operator = condition["op"]
            value = condition["value"]
            if operator not in VALID_OPERATORS:
                raise ValueError(f"Invalid operator in condition: {operator}")
            if not self._compare(self.snapshot.state.get(key), operator, value):
                return False
        return True

    def get_current_node(self) -> dict[str, Any]:
        return self.node_map[self.snapshot.current_node_id]

    def available_choices(self, node: dict[str, Any]) -> list[dict[str, Any]]:
        return [
            choice
            for choice in node.get("choices", [])
            if self.conditions_met(choice.get("conditions"))
        ]

    def apply_effects(self, effects: list[dict[str, Any]] | None) -> None:
        if not effects:
            return
        for effect in effects:
            key = effect["key"]
            mode = effect.get("mode", "set")
            value = effect["value"]
            if mode == "set":
                self.snapshot.state[key] = value
            elif mode == "add":
                self.snapshot.state[key] = self.snapshot.state.get(key, 0) + value
            elif mode == "append_unique":
                bucket = self.snapshot.state.setdefault(key, [])
                if value not in bucket:
                    bucket.append(value)
            elif mode == "max":
                self.snapshot.state[key] = max(self.snapshot.state.get(key, value), value)
            else:
                raise ValueError(f"Invalid effect mode: {mode}")

    def choose(self, index: int) -> None:
        node = self.get_current_node()
        choices = self.available_choices(node)
        if index < 0 or index >= len(choices):
            raise IndexError("Choice out of range")
        selected = choices[index]
        self.apply_effects(selected.get("effects"))
        self.snapshot.current_node_id = selected["next"]
        self.snapshot.history.append(self.snapshot.current_node_id)

    def step_with_choice(self, index: int) -> dict[str, Any]:
        self.choose(index)
        return self.get_current_node()

    def is_ending(self, node: dict[str, Any] | None = None) -> bool:
        target = node or self.get_current_node()
        return target.get("type") == "ending"

    def _show_scene(self) -> list[dict[str, Any]]:
        node = self.get_current_node()
        choices = self.available_choices(node)
        tier = int(self.snapshot.state.get("memory_tier", 0))
        self.renderer.render_scene(node, choices, tier)
        return choices

    def run(self) -> None:
        self.renderer.render_status("SYS: SCP-079 REMAKE // :save <file> // :load <file>")
        while True:
            node = self.get_current_node()
            choices = self._show_scene()

            if self.is_ending(node):
                self.renderer.render_status("--- END ---", level="warning")
                return

            if not choices:
                self.renderer.render_status("No valid choices. Story stopped.", level="warning")
                return

            raw = input("> ").strip()
            if raw.startswith(":save"):
                _, *rest = raw.split(maxsplit=1)
                file_name = rest[0] if rest else "savegame.json"
                self.save(file_name)
                self.renderer.render_status(f"SYS: Save written: {file_name}")
                continue
            if raw.startswith(":load"):
                _, *rest = raw.split(maxsplit=1)
                file_name = rest[0] if rest else "savegame.json"
                self.load(file_name)
                self.renderer.render_status(f"SYS: Save loaded: {file_name}")
                continue
            if raw == ":status":
                state = self.snapshot.state
                self.renderer.render_status(
                    (
                        "SYS: "
                        f"trust={state['trust_with_079']} alert={state['foundation_alert']} "
                        f"injury={state['injury']} battery={state['battery_power']} "
                        f"memory={state['memory_tier']} trace={state['mtf_trace_progress']}"
                    )
                )
                continue

            if not raw.isdigit():
                self.renderer.render_status("SYS: Input rejected.", level="warning")
                continue

            self.choose(int(raw) - 1)
