from pathlib import Path

from scp079.engine import StoryEngine
from scp079.renderer import TerminalRenderer
from scp079.story import DEFAULT_STATE, START_NODE, STORY_NODES


def test_save_and_load_roundtrip(tmp_path: Path):
    engine = StoryEngine(
        STORY_NODES,
        START_NODE,
        DEFAULT_STATE,
        renderer=TerminalRenderer(seed=2),
    )
    engine.choose(0)
    engine.choose(0)
    engine.choose(0)

    save_file = tmp_path / "save.json"
    engine.save(save_file)

    clone = StoryEngine(
        STORY_NODES,
        START_NODE,
        DEFAULT_STATE,
        renderer=TerminalRenderer(seed=2),
    )
    clone.load(save_file)

    assert clone.snapshot.current_node_id == engine.snapshot.current_node_id
    assert clone.snapshot.state == engine.snapshot.state
    assert clone.snapshot.history == engine.snapshot.history
