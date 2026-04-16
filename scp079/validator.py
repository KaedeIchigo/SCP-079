from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from scp079.engine import VALID_OPERATORS


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def validate_story(story_nodes: list[dict[str, Any]], start_node: str) -> ValidationReport:
    report = ValidationReport()
    ids = [n["id"] for n in story_nodes]

    seen: set[str] = set()
    duplicates: set[str] = set()
    for node_id in ids:
        if node_id in seen:
            duplicates.add(node_id)
        seen.add(node_id)
    if duplicates:
        report.errors.append(f"Duplicate node ids: {sorted(duplicates)}")

    node_map = {node["id"]: node for node in story_nodes}
    if start_node not in node_map:
        report.errors.append(f"Start node missing: {start_node}")
        return report

    for node in story_nodes:
        for choice in node.get("choices", []):
            next_id = choice.get("next")
            if next_id not in node_map:
                report.errors.append(
                    f"Node {node['id']} has missing next reference: {next_id}"
                )
            for condition in choice.get("conditions", []):
                if condition.get("op") not in VALID_OPERATORS:
                    report.errors.append(
                        f"Node {node['id']} invalid condition operator: {condition.get('op')}"
                    )
                if "key" not in condition or "value" not in condition:
                    report.errors.append(f"Node {node['id']} has malformed condition: {condition}")

    reachable = set()
    stack = [start_node]
    while stack:
        node_id = stack.pop()
        if node_id in reachable:
            continue
        reachable.add(node_id)
        node = node_map.get(node_id)
        if node is None:
            continue
        for choice in node.get("choices", []):
            stack.append(choice["next"])

    endings = [n["id"] for n in story_nodes if n.get("type") == "ending"]
    unreachable_endings = sorted([e for e in endings if e not in reachable])
    if unreachable_endings:
        report.errors.append(f"Unreachable endings: {unreachable_endings}")

    orphan_non_endings = [
        node_id
        for node_id in node_map
        if node_id not in reachable and node_map[node_id].get("type") != "ending"
    ]
    if orphan_non_endings:
        report.warnings.append(f"Unreachable non-ending nodes: {sorted(orphan_non_endings)}")

    return report


def main() -> int:
    from scp079.story import START_NODE, STORY_NODES

    report = validate_story(STORY_NODES, START_NODE)
    if report.errors:
        print("VALIDATION FAILED")
        for err in report.errors:
            print(f"ERROR: {err}")
    else:
        print("VALIDATION OK")

    for warning in report.warnings:
        print(f"WARN: {warning}")

    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
