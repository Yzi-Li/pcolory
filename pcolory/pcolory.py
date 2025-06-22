# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/Yzi-Li/pcolory/blob/main/copyright.txt


from typing import Dict
from .colors import Color, RESET

BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
INVERSE = "\033[7m"
CONCEAL = "\033[8m"
CROSSED_OUT = "\033[9m"

type OptionalColor = Color | None
type OptionalBool = bool | None
type OptionalStr = str | None
type ConfigValue = bool | Color | None
type ConfigDict = Dict[str, ConfigValue]

DEFAULT_CONFIG: ConfigDict = {
    "enable": True,
    "fg": None,
    "bg": None,
    "bold": None,
    "faint": None,
    "italic": None,
    "underline": None,
    "blink": None,
    "inverse": None,
    "conceal": None,
    "crossed_out": None,
}


DEFAULT_CONFIG_VALUES: Dict[str, str] = {
    "bold": BOLD,
    "faint": FAINT,
    "italic": ITALIC,
    "underline": UNDERLINE,
    "blink": BLINK,
    "inverse": INVERSE,
    "conceal": CONCEAL,
    "crossed_out": CROSSED_OUT,
}


class Config:
    enable: bool = True
    fg: OptionalColor = None
    bg: OptionalColor = None
    bold: OptionalBool = None
    faint: OptionalBool = None
    italic: OptionalBool = None
    underline: OptionalBool = None
    blink: OptionalBool = None
    inverse: OptionalBool = None
    conceal: OptionalBool = None
    crossed_out: OptionalBool = None
    _code: str = ""

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            self.__setattr__(key, val)


def get_code(cfg: Config) -> str:
    code = ""
    cfg_dict = DEFAULT_CONFIG | cfg.__dict__

    code += cfg_dict["fg"].code if cfg_dict["fg"] is not None else ""
    code += cfg_dict["bg"].code if cfg_dict["bg"] is not None else ""

    del cfg_dict["enable"], cfg_dict["fg"], cfg_dict["bg"]

    for key, val in cfg_dict.items():
        code += DEFAULT_CONFIG_VALUES[key] if val else ""

    return code.replace("m\033[", ";")


class ColorPrint:
    def __init__(self):
        self._config = Config()

    def __call__(
            self,
            *values: object,
            fg: OptionalColor = None,
            bg: OptionalColor = None,
            bold: OptionalBool = None,
            faint: OptionalBool = None,
            italic: OptionalBool = None,
            underline: OptionalBool = None,
            blink: OptionalBool = None,
            inverse: OptionalBool = None,
            conceal: OptionalBool = None,
            crossed_out: OptionalBool = None,
            sep: OptionalStr = None,
            end: OptionalStr = None
    ) -> None:

        if not self._config.enable:
            print(*values, sep=sep, end=end)
            return

        if fg is not None and fg.is_bg:
            raise ValueError(
                "fg must be foreground color, not background color."
            )
        if bg is not None and not bg.is_bg:
            raise ValueError(
                "bg must be background color, not foreground color."
            )

        fg = fg or self._config.fg
        bg = bg or self._config.bg
        bold = bold or self._config.bold
        faint = faint or self._config.faint
        italic = italic or self._config.italic
        underline = underline or self._config.underline
        blink = blink or self._config.blink
        inverse = inverse or self._config.inverse
        conceal = conceal or self._config.conceal
        crossed_out = crossed_out or self._config.crossed_out

        code = get_code(
            Config(
                fg=fg,
                bg=bg,
                bold=bold,
                faint=faint,
                italic=italic,
                underline=underline,
                blink=blink,
                inverse=inverse,
                conceal=conceal,
                crossed_out=crossed_out
            )
        )

        print(code, end="")
        print(*values, sep=sep, end="")

        if end is None:
            print(f"{RESET}\n", end="")
            return

        end_list = end.splitlines()

        for i, val in enumerate(end_list):
            if i < len(end_list) - 1:
                print(f"{val}{RESET}\n{code}", end="")
            else:
                print(val, end=RESET)

    def config(self, cfg: ConfigDict = {}, **kwargs) -> None:
        if isinstance(cfg, dict):
            for key, val in cfg.items():
                self._config.__setattr__(key, val)

        for key, val in kwargs.items():
            self._config.__setattr__(key, val)

        self._config.__setattr__("_code", get_code(self._config))
