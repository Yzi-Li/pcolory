# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/Yzi-Li/pcolory/blob/main/copyright.txt


import io
from contextlib import redirect_stdout

from .colorprinttest import ColorPrintTest
from pcolory import colorprint
from pcolory.colors import FG_BLACK, BG_RED, RESET

fg = FG_BLACK
bg = BG_RED
fg_code = fg.code
bg_code = bg.code


class TestColorPrint(ColorPrintTest):
    def test_colorprint(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello, World!", fg=fg, bg=bg)
            out = buf.getvalue()
        self.assertEqual(f"{fg_code}{bg_code}Hello, World!{RESET}\n", out)

    def test_multiple(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello,", "World!", fg=fg, bg=bg)
            out = buf.getvalue()
        self.assertEqual(f"{fg_code}{bg_code}Hello, World!{RESET}\n", out)

    def test_sep_end(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello", "World", fg=fg, bg=bg, sep=", ", end="!\n!")
            out = buf.getvalue()
        self.assertEqual(f"{fg_code}{bg_code}Hello, World!{RESET}\n{fg_code}\
                         {bg_code}!{RESET}", out)

        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello", "World!", fg=fg, bg=bg, sep=", ", end=None)
            out = buf.getvalue()
        self.assertEqual(f"{fg_code}{bg_code}Hello, World!{RESET}\n", out)

    def test_fg_bg_error(self):
        with self.assertRaises(ValueError):
            colorprint("Hello, World!", fg=bg)

        with self.assertRaises(ValueError):
            colorprint("Hello, World!", bg=fg)
