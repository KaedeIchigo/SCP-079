from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


VALID_OPERATORS = {"==", "!=", ">", "<", ">=", "<=", "in", "not_in", "contains", "contains_all"}


@dataclass
class EngineSnapshot:
    current_node_id: str
    state: dict[str, Any]


class StoryEngine:
    def __init__(
        self,
        story_nodes: list[dict[str, Any]],
        start_node: str,
        default_state: dict[str, Any],
    ) -> None:
        self.story_nodes = story_nodes
        self.node_map: dict[str, dict[str, Any]] = {n["id"]: n for n in story_nodes}
        self.start_node = start_node
        self.default_state = default_state
        self.snapshot = EngineSnapshot(current_node_id=start_node, state=dict(default_state))

    def reset(self) -> None:
        self.snapshot = EngineSnapshot(
            current_node_id=self.start_node,
            state=dict(self.default_state),
        )

    def save(self, path: str | Path) -> None:
        data = {
            "current_node_id": self.snapshot.current_node_id,
            "state": self.snapshot.state,
        }
        Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")

    def load(self, path: str | Path) -> None:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        self.snapshot = EngineSnapshot(
            current_node_id=data["current_node_id"],
            state=data["state"],
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

    def step_with_choice(self, index: int) -> dict[str, Any]:
        self.choose(index)
        return self.get_current_node()

    def is_ending(self, node: dict[str, Any] | None = None) -> bool:
        target = node or self.get_current_node()
        return target.get("type") == "ending"

    def run(self) -> None:
        print("SCP-079 REMAKE // terminal story // type :save <file> or :load <file>")
        print("=================================================================")
        while True:
            node = self.get_current_node()
            print(f"\n[{node['act']}] {node['title']}")
            for line in node.get("text", []):
                print(line)

            if self.is_ending(node):
                print("\n--- END ---")
                return

            choices = self.available_choices(node)
            if not choices:
                print("No valid choices. Story stopped.")
                return

            for i, choice in enumerate(choices, start=1):
                print(f"{i}. {choice['text']}")

            raw = input("> ").strip()
            if raw.startswith(":save"):
                _, *rest = raw.split(maxsplit=1)
                file_name = rest[0] if rest else "savegame.json"
                self.save(file_name)
                print(f"Saved to {file_name}")
                continue
            if raw.startswith(":load"):
                _, *rest = raw.split(maxsplit=1)
                file_name = rest[0] if rest else "savegame.json"
                self.load(file_name)
                print(f"Loaded from {file_name}")
                continue

            if not raw.isdigit():
                print("Input rejected.")
                continue

            self.choose(int(raw) - 1)
