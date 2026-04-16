from scp079.renderer import CLEAR_SEQUENCE, TerminalRenderer


def test_renderer_clear_sequence():
    renderer = TerminalRenderer()
    seq = renderer.clear()
    assert seq == CLEAR_SEQUENCE
    assert "\033[2J" in seq and "\033[H" in seq
