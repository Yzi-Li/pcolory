# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/Yzi-Li/pcolory/blob/main/copyright.txt


from typing import Dict
from .colors import Color, RESET


class Config:
    enable: bool = True
    fg: Color | str = ""
    bg: Color | str = ""


class ColorPrint:
    def __init__(self):
        self._config = Config()

    def __call__(self, *values: object,
                 fg: Color | str = "",
                 bg: Color | str = "",
                 sep: str | None = "",
                 end: str | None = "\n"):
        if not self._config.enable:
            print(*values, sep=sep, end=end)
            return

        fg = fg or self._config.fg
        bg = bg or self._config.bg
        code = f"{fg}{bg}"

        print(code, end="")
        print(*values, sep=sep, end="")

        if end is None:
            end = "\n"
        for i in end.splitlines():
            print(f"{i}{RESET}\n{code}", end="")
        print(RESET, end="")

    def config(self, cfg: Dict[str, bool] = {}, **kwargs):
        if isinstance(cfg, dict):
            for key, val in cfg.items():
                self._config.__setattr__(key, val)

        for key, val in kwargs.items():
            self._config.__setattr__(key, val)
