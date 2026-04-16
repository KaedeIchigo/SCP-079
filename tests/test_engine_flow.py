from scp079.engine import StoryEngine
from scp079.story import DEFAULT_STATE, START_NODE, STORY_NODES


def make_engine() -> StoryEngine:
    return StoryEngine(STORY_NODES, START_NODE, DEFAULT_STATE)


def test_engine_progresses_to_ending():
    engine = make_engine()
    path = [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]  # thermonuclear path
    for step in path:
        node = engine.get_current_node()
        if engine.is_ending(node):
            break
        engine.choose(step)

    assert engine.is_ending(engine.get_current_node())
    assert engine.get_current_node()["id"] == "ending_thermonuclear"


def test_condition_hides_true_ending_without_secrets():
    engine = make_engine()
    # move quickly to act4_revelation without secret nodes
    forced = [0, 0, 0, 0, 0, 0, 0, 1, 1]
    for step in forced:
        engine.choose(step)

    node = engine.get_current_node()
    choices = engine.available_choices(node)
    texts = {choice["text"] for choice in choices}
    assert all("deep memory wipe" not in text for text in texts)
