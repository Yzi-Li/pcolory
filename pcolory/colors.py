# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/Yzi-Li/pcolory/blob/main/copyright.txt


from copy import deepcopy
from typing import Dict, Tuple


class Color:
    def classic(self, code: int, bright: bool = False) -> "Color":
        base: int = 30 + bright * 60
        self.fg = f"\033[{base + code}m"
        self.bg = f"\033[{base + 10 + code}m"
        return deepcopy(self)

    def rgb(self, rgb_tuple: Tuple[int, int, int]) -> "Color":
        base: int = 38
        r, g, b = rgb_tuple
        self.fg = f"\033[{base};2;{r};{g};{b}m"
        self.bg = f"\033[{base + 10};2;{r};{g};{b}m"
        return deepcopy(self)


_color = Color()

RESET: str = "\033[0m"

CLASSIC_COLORS = (
    "BLACK",
    "RED",
    "GREEN",
    "YELLOW",
    "BLUE",
    "MAGENTA",
    "CYAN",
    "WHITE"
)

COLORS: Dict[str, Color] = {}

for code, name in enumerate(CLASSIC_COLORS):
    COLORS[f"{name}"] = _color.classic(code)
    COLORS[f"BRIGHT_{name}"] = _color.classic(code, True)

# Classic colors
BLACK = COLORS["BLACK"]
RED = COLORS["RED"]
GREEN = COLORS["GREEN"]
YELLOW = COLORS["YELLOW"]
BLUE = COLORS["BLUE"]
MAGENTA = COLORS["MAGENTA"]
CYAN = COLORS["CYAN"]
WHITE = COLORS["WHITE"]
BLACK = COLORS["BLACK"]

# Bright colors
BRIGHT_RED = COLORS["BRIGHT_RED"]
BRIGHT_GREEN = COLORS["BRIGHT_GREEN"]
BRIGHT_YELLOW = COLORS["BRIGHT_YELLOW"]
BRIGHT_BLUE = COLORS["BRIGHT_BLUE"]
BRIGHT_MAGENTA = COLORS["BRIGHT_MAGENTA"]
BRIGHT_CYAN = COLORS["BRIGHT_CYAN"]
BRIGHT_WHITE = COLORS["BRIGHT_WHITE"]
