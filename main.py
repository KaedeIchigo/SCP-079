from scp079.engine import StoryEngine
from scp079.story import STORY_NODES, START_NODE, DEFAULT_STATE


def main() -> None:
    engine = StoryEngine(
        story_nodes=STORY_NODES,
        start_node=START_NODE,
        default_state=DEFAULT_STATE,
    )
    engine.run()


if __name__ == "__main__":
    main()
