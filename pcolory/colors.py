# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/Yzi-Li/pcolory/blob/main/copyright.txt


from copy import deepcopy
from typing import Dict, List, Tuple


class Color:
    def __init__(self, is_bg: bool = False):
        self.is_bg = is_bg

    def ansi(self, code: int, bright: bool = False) -> "Color":
        base: int = 30 + self.is_bg * 10 + bright * 60
        self.code = f"\033[{base + code}m"
        return deepcopy(self)

    def rgb(self, rgb_tuple: Tuple[int, int, int]) -> "Color":
        base: int = 38 + self.is_bg * 10
        r, g, b = rgb_tuple
        self.code = f"\033[{base};2;{r};{g};{b}m"
        return deepcopy(self)


fg_color = Color()
bg_color = Color(True)

RESET: str = fg_color.ansi(-30).code  # \033[0m

color_names: List[str] = [
    "BLACK",
    "RED",
    "GREEN",
    "YELLOW",
    "BLUE",
    "MAGENTA",
    "CYAN",
    "WHITE"
]

COLORS: Dict[str, Color] = {}

for code, name in enumerate(color_names):
    COLORS[f"FG_{name}"] = fg_color.ansi(code)
    COLORS[f"FG_BRIGHT_{name}"] = fg_color.ansi(code, True)
    COLORS[f"BG_{name}"] = bg_color.ansi(code)
    COLORS[f"BG_BRIGHT_{name}"] = bg_color.ansi(code, True)

# Foreground colors
FG_BLACK = COLORS["FG_BLACK"]
FG_RED = COLORS["FG_RED"]
FG_GREEN = COLORS["FG_GREEN"]
FG_YELLOW = COLORS["FG_YELLOW"]
FG_BLUE = COLORS["FG_BLUE"]
FG_MAGENTA = COLORS["FG_MAGENTA"]
FG_CYAN = COLORS["FG_CYAN"]
FG_WHITE = COLORS["FG_WHITE"]
FG_BRIGHT_BLACK = COLORS["FG_BRIGHT_BLACK"]

# Bright foreground colors
FG_BRIGHT_RED = COLORS["FG_BRIGHT_RED"]
FG_BRIGHT_GREEN = COLORS["FG_BRIGHT_GREEN"]
FG_BRIGHT_YELLOW = COLORS["FG_BRIGHT_YELLOW"]
FG_BRIGHT_BLUE = COLORS["FG_BRIGHT_BLUE"]
FG_BRIGHT_MAGENTA = COLORS["FG_BRIGHT_MAGENTA"]
FG_BRIGHT_CYAN = COLORS["FG_BRIGHT_CYAN"]
FG_BRIGHT_WHITE = COLORS["FG_BRIGHT_WHITE"]

# Background colors
BG_BLACK = COLORS["BG_BLACK"]
BG_RED = COLORS["BG_RED"]
BG_GREEN = COLORS["BG_GREEN"]
BG_YELLOW = COLORS["BG_YELLOW"]
BG_BLUE = COLORS["BG_BLUE"]
BG_MAGENTA = COLORS["BG_MAGENTA"]
BG_CYAN = COLORS["BG_CYAN"]
BG_WHITE = COLORS["BG_WHITE"]

# Bright background colors
BG_BRIGHT_BLACK = COLORS["BG_BRIGHT_BLACK"]
BG_BRIGHT_RED = COLORS["BG_BRIGHT_RED"]
BG_BRIGHT_GREEN = COLORS["BG_BRIGHT_GREEN"]
BG_BRIGHT_YELLOW = COLORS["BG_BRIGHT_YELLOW"]
BG_BRIGHT_BLUE = COLORS["BG_BRIGHT_BLUE"]
BG_BRIGHT_MAGENTA = COLORS["BG_BRIGHT_MAGENTA"]
BG_BRIGHT_CYAN = COLORS["BG_BRIGHT_CYAN"]
BG_BRIGHT_WHITE = COLORS["BG_BRIGHT_WHITE"]
