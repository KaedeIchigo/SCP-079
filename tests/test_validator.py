from copy import deepcopy

from scp079.story import START_NODE, STORY_NODES
from scp079.validator import validate_story


def test_validator_ok_on_main_story():
    report = validate_story(STORY_NODES, START_NODE)
    assert report.ok, report.errors


def test_validator_catches_missing_node_reference():
    broken = deepcopy(STORY_NODES)
    broken[0]["choices"][0]["next"] = "missing"
    report = validate_story(broken, START_NODE)
    assert any("missing next reference" in err for err in report.errors)


def test_validator_catches_duplicate_ids():
    broken = deepcopy(STORY_NODES)
    broken.append(deepcopy(broken[0]))
    report = validate_story(broken, START_NODE)
    assert any("Duplicate node ids" in err for err in report.errors)
