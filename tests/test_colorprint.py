# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/Yzi-Li/pcolory/blob/main/copyright.txt


import io
from contextlib import redirect_stdout

from .colorprinttest import ColorPrintTest
from pcolory import colorprint, color
from pcolory.colors import BLACK, RED

fg = BLACK
bg = RED


class TestColorPrint(ColorPrintTest):
    def test_colorprint(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello, World!", fg=fg, bg=bg)
            out = buf.getvalue()
        self.assertEqual("\033[30;41mHello, World!\033[0m\n", out)

    def test_multiple(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello,", "World!", fg=fg, bg=bg)
            out = buf.getvalue()
        self.assertEqual("\033[30;41mHello, World!\033[0m\n", out)

    def test_sep_end(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello", "World", fg=fg, bg=bg, sep=", ", end="!\n!")
            out = buf.getvalue()
        self.assertEqual(
            "\033[30;41mHello, World!\033[0m\n\033[30;41m!\033[0m", out
        )

        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello", "World!", fg=fg, bg=bg, sep=", ", end=None)
            out = buf.getvalue()
        self.assertEqual("\033[30;41mHello, World!\033[0m\n", out)

    def test_rgb_hex(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello, World!", fg=color("rgb", (255, 0, 0)))
            out = buf.getvalue()
        self.assertEqual("\033[38;2;255;0;0mHello, World!\033[0m\n", out)

        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello, World!", fg=color("hex", "#FF0000"))
            out = buf.getvalue()
        self.assertEqual("\033[38;2;255;0;0mHello, World!\033[0m\n", out)

        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello, World!", fg=color("hex", "#F00"))
            out = buf.getvalue()
        self.assertEqual("\033[38;2;255;0;0mHello, World!\033[0m\n", out)

    def test_rgb_hex_error(self):
        with self.assertRaises(ValueError) as e:
            colorprint("Hello, World!", fg=color("rgb", [255, 0, 0]))
        self.assertEqual("Expected tuple, got list", str(e.exception))

        with self.assertRaises(ValueError) as e:
            colorprint("Hello, World!", fg=color("hex", 0xFF0000))
        self.assertEqual("Expected str, got int", str(e.exception))

        with self.assertRaises(ValueError) as e:
            colorprint("Hello, World!", fg=color("rgba", (255, 0, 0, 0.5)))
        self.assertEqual("mode must be 'rgb' or 'hex'", str(e.exception))
