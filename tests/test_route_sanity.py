from collections import deque

from scp079.story import START_NODE, STORY_NODES


def _shortest_to_any_ending() -> int:
    node_map = {n["id"]: n for n in STORY_NODES}
    q = deque([(START_NODE, 0)])
    seen = {START_NODE}
    while q:
        node_id, depth = q.popleft()
        node = node_map[node_id]
        if node.get("type") == "ending":
            return depth
        for choice in node.get("choices", []):
            nxt = choice["next"]
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, depth + 1))
    return -1


def test_legacy_route_beats_exist():
    ids = {n["id"] for n in STORY_NODES}
    required = {
        "a1_login_prompt",
        "a1_awakening",
        "a1_q_682",
        "a1_breach_initiation",
        "a2_forced_alliance",
        "a2_laptop_transfer",
        "a3_city_arrival",
        "a3_battery_collapse",
        "a4_safehouse_entry",
    }
    assert required.issubset(ids)


def test_has_required_endings():
    ids = {n["id"] for n in STORY_NODES}
    required_endings = {
        "ending_mtf_grim_good",
        "ending_079_betrayal",
        "ending_thermonuclear",
        "ending_682_catastrophe",
        "end_emp_burn",
        "ending_ambiguous",
        "ending_true_bleak",
    }
    assert required_endings.issubset(ids)


def test_shortest_route_is_not_tiny():
    depth = _shortest_to_any_ending()
    assert depth >= 13
