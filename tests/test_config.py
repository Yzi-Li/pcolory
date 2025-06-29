# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/Yzi-Li/pcolory/blob/main/copyright.txt


import io
from contextlib import redirect_stdout

from .colorprinttest import ColorPrintTest
from pcolory import config, colorprint
from pcolory.colors import BLACK, RED

fg = BLACK
bg = RED


class TestConfig(ColorPrintTest):
    def test_enable(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            config(enable=False)
            colorprint("Hello, World!", fg=fg, bg=bg)
            out = buf.getvalue()
        self.assertEqual("Hello, World!\n", out)

        with io.StringIO() as buf, redirect_stdout(buf):
            config({"enable": False})
            colorprint("Hello, World!", fg=fg, bg=bg)
            out = buf.getvalue()
        self.assertEqual("Hello, World!\n", out)

    def test_fg_bg(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            config(fg=fg, bg=bg)
            colorprint("Hello, World!")
            out = buf.getvalue()
        self.assertEqual("\033[30;41mHello, World!\033[0m\n", out)

        with io.StringIO() as buf, redirect_stdout(buf):
            config({"fg": fg, "bg": bg})
            colorprint("Hello, World!")
            out = buf.getvalue()
        self.assertEqual("\033[30;41mHello, World!\033[0m\n", out)
