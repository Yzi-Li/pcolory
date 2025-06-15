# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/Yzi-Li/pcolory/blob/main/copyright.txt


from typing import Dict
from .colors import Color, RESET


class Config:
    enable: bool = True
    fg: Color | None = None
    bg: Color | None = None


class ColorPrint:
    def __init__(self):
        self._config = Config()

    def __call__(self, *values: object,
                 fg: Color | None = None,
                 bg: Color | None = None,
                 sep: str | None = None,
                 end: str | None = None):
        if not self._config.enable:
            print(*values, sep=sep, end=end)
            return

        if fg is not None and fg.is_bg:
            raise ValueError("fg must be foreground color, not background color.")
        if bg is not None and not bg.is_bg:
            raise ValueError("bg must be background color, not foreground color.")

        fg_code: str = "" if fg is None and self._config.fg is None else (fg or self._config.fg).code
        bg_code: str = "" if bg is None and self._config.bg is None else (bg or self._config.bg).code
        code = f"{fg_code}{bg_code}"

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

    def config(self, cfg: Dict[str, bool] = {}, **kwargs):
        if isinstance(cfg, dict):
            for key, val in cfg.items():
                self._config.__setattr__(key, val)

        for key, val in kwargs.items():
            self._config.__setattr__(key, val)
