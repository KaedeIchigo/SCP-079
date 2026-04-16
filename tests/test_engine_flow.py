from scp079.engine import StoryEngine
from scp079.renderer import TerminalRenderer
from scp079.story import DEFAULT_STATE, START_NODE, STORY_NODES


def make_engine() -> StoryEngine:
    return StoryEngine(
        STORY_NODES,
        START_NODE,
        DEFAULT_STATE,
        renderer=TerminalRenderer(seed=1),
    )


def test_engine_progresses_to_thermonuclear_ending():
    engine = make_engine()
    path = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ]
    for step in path:
        if engine.is_ending(engine.get_current_node()):
            break
        engine.choose(step)

    assert engine.is_ending(engine.get_current_node())
    assert engine.get_current_node()["id"] == "ending_thermonuclear"


def test_true_bleak_choice_hidden_without_required_secrets():
    engine = make_engine()
    # Route that reaches operation hub without both mirror_cache and relay_notes_copy.
    path_to_hub = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
        0, 0, 0, 0, 0, 0, 0
    ]
    for step in path_to_hub:
        engine.choose(step)

    node = engine.get_current_node()
    assert node["id"] == "a5_operation_hub"
    options = [c["text"] for c in engine.available_choices(node)]
    assert not any("local containment" in text.lower() for text in options)
