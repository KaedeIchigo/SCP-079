from __future__ import annotations

import random
import sys
import time
from dataclasses import dataclass
from typing import Iterable


CLEAR_SEQUENCE = "\033[2J\033[H"
RESET = "\033[0m"

COLORS = {
    "system": "\033[92m",
    "narration": "\033[37m",
    "choice": "\033[96m",
    "warning": "\033[91m",
    "tier0": "\033[95m",
    "tier1": "\033[35m",
    "tier2": "\033[94m",
    "tier3": "\033[36m",
    "tier4": "\033[31m",
    "corrupt": "\033[33m",
}


@dataclass
class RenderConfig:
    typing_delay: float = 0.0
    glitch_chance: float = 0.08


class TerminalRenderer:
    def __init__(self, config: RenderConfig | None = None, seed: int = 79) -> None:
        self.config = config or RenderConfig()
        self._rng = random.Random(seed)

    def clear(self) -> str:
        sys.stdout.write(CLEAR_SEQUENCE)
        sys.stdout.flush()
        return CLEAR_SEQUENCE

    def _write_line(self, text: str, color: str) -> None:
        sys.stdout.write(f"{color}{text}{RESET}\n")
        sys.stdout.flush()
        if self.config.typing_delay:
            time.sleep(self.config.typing_delay)

    def _scramble(self, text: str) -> str:
        chars = list(text)
        for i, ch in enumerate(chars):
            if ch != " " and self._rng.random() < 0.18:
                chars[i] = self._rng.choice("#@$%01/\\")
        return "".join(chars)

    def _tier_color(self, memory_tier: int) -> str:
        return {
            0: COLORS["tier0"],
            1: COLORS["tier1"],
            2: COLORS["tier2"],
            3: COLORS["tier3"],
        }.get(memory_tier, COLORS["tier4"])

    def render_header(self, act: str, title: str, memory_tier: int) -> None:
        top = f"[{act}] {title}"
        if memory_tier >= 4:
            top = f"<{act} :: {title} :: OWNED>"
        self._write_line(top, COLORS["system"])
        self._write_line("-" * min(72, len(top) + 8), COLORS["system"])

    def render_text(self, lines: Iterable[str], memory_tier: int) -> None:
        for line in lines:
            if line.startswith("079:"):
                color = self._tier_color(memory_tier)
                if memory_tier >= 3 and self._rng.random() < self.config.glitch_chance:
                    line = self._scramble(line)
                self._write_line(line, color)
            elif line.startswith("SYS:"):
                self._write_line(line, COLORS["system"])
            elif line.startswith("CORRUPT:"):
                self._write_line(self._scramble(line), COLORS["corrupt"])
            else:
                self._write_line(line, COLORS["narration"])

    def render_choices(self, choices: list[dict[str, str]], memory_tier: int) -> None:
        color = COLORS["choice"] if memory_tier < 4 else COLORS["warning"]
        for i, choice in enumerate(choices, start=1):
            text = choice["text"]
            if memory_tier >= 4 and i == len(choices):
                text = f"{text} [INPUT OBSERVED]"
            self._write_line(f"{i}. {text}", color)

    def render_scene(self, node: dict, choices: list[dict[str, str]], memory_tier: int) -> None:
        self.clear()
        self.render_header(node["act"], node["title"], memory_tier)
        self.render_text(node.get("text", []), memory_tier)
        if choices:
            self._write_line("", COLORS["narration"])
            self.render_choices(choices, memory_tier)

    def render_status(self, message: str, level: str = "system") -> None:
        color = COLORS.get(level, COLORS["system"])
        self._write_line(message, color)
