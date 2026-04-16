from scp079.story import STORY_NODES


def test_legacy_route_beats_exist():
    ids = {n["id"] for n in STORY_NODES}
    required = {
        "boot_auth",
        "awake_079",
        "q_682",
        "breach_trigger",
        "forced_alliance",
        "car_escape",
        "atm_withdrawal",
        "battery_drain",
        "safehouse_entry",
    }
    assert required.issubset(ids)


def test_has_required_endings():
    ids = {n["id"] for n in STORY_NODES}
    required_endings = {
        "ending_mtf_capture",
        "ending_079_betrayal",
        "ending_thermonuclear",
        "ending_682_catastrophe",
        "end_death_hallway",
        "ending_ambiguous",
        "ending_true_bleak",
    }
    assert required_endings.issubset(ids)
