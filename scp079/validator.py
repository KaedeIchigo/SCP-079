from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass, field
from typing import Any

from scp079.engine import VALID_OPERATORS


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not self.errors


def _shortest_depths(node_map: dict[str, dict[str, Any]], start_node: str) -> dict[str, int]:
    depths = {start_node: 0}
    queue = deque([start_node])
    while queue:
        node_id = queue.popleft()
        depth = depths[node_id]
        for choice in node_map[node_id].get("choices", []):
            nxt = choice["next"]
            if nxt not in depths:
                depths[nxt] = depth + 1
                if nxt in node_map:
                    queue.append(nxt)
    return depths


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

    effect_counter: Counter[str] = Counter()
    indegree: Counter[str] = Counter()

    for node in story_nodes:
        for choice in node.get("choices", []):
            next_id = choice.get("next")
            indegree[next_id] += 1
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
            for effect in choice.get("effects", []):
                if "key" in effect:
                    effect_counter[effect["key"]] += 1

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
    non_endings = [n["id"] for n in story_nodes if n.get("type") != "ending"]

    unreachable_endings = sorted([e for e in endings if e not in reachable])
    if unreachable_endings:
        report.errors.append(f"Unreachable endings: {unreachable_endings}")

    if len(non_endings) < 35:
        report.errors.append(f"Non-ending scene count too low: {len(non_endings)} (min 35)")

    depths = _shortest_depths(node_map, start_node)
    ending_depths = [depths[e] for e in endings if e in depths]
    if ending_depths:
        min_end_depth = min(ending_depths)
        if min_end_depth < 14:
            report.warnings.append(
                f"Shortest route to ending is shallow ({min_end_depth} scenes)."
            )
    else:
        min_end_depth = None

    heavy_early_reconvergence = [
        node_id for node_id, deg in indegree.items() if deg >= 3 and depths.get(node_id, 999) <= 10
    ]
    if heavy_early_reconvergence:
        report.warnings.append(
            "Heavy early reconvergence at nodes: "
            + ", ".join(sorted(heavy_early_reconvergence))
        )

    quick_branch_nodes = []
    for node in story_nodes:
        choices = node.get("choices", [])
        if len(choices) < 2:
            continue
        target_depths = []
        for choice in choices:
            nxt = choice["next"]
            if nxt in node_map and node_map[nxt].get("type") == "ending":
                target_depths.append(1)
            elif nxt in node_map:
                sub = _shortest_depths(node_map, nxt)
                end_sub = [sub[e] for e in endings if e in sub]
                if end_sub:
                    target_depths.append(min(end_sub) + 1)
        if target_depths and max(target_depths) <= 3:
            quick_branch_nodes.append(node["id"])

    if quick_branch_nodes:
        report.warnings.append(
            "Branches resolving too quickly after decision nodes: "
            + ", ".join(sorted(quick_branch_nodes))
        )

    underused_state_keys = sorted([key for key, count in effect_counter.items() if count <= 1])
    if underused_state_keys:
        report.warnings.append(
            "Potentially underused state variables (<=1 effect): "
            + ", ".join(underused_state_keys)
        )

    report.metrics = {
        "total_nodes": len(story_nodes),
        "non_ending_nodes": len(non_endings),
        "ending_nodes": len(endings),
        "reachable_nodes": len(reachable),
        "shortest_ending_depth": min_end_depth,
        "max_depth": max(depths.values()) if depths else 0,
    }

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

    print("METRICS:")
    for key, value in report.metrics.items():
        print(f"- {key}: {value}")

    for warning in report.warnings:
        print(f"WARN: {warning}")

    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
