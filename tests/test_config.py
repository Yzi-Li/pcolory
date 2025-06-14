# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/Yzi-Li/pcolory/blob/main/copyright.txt


import io
from contextlib import redirect_stdout

from .colorprinttest import ColorPrintTest
from pcolory import config, colorprint
from pcolory.colors import FG_BLACK, BG_RED, RESET


class TestConfig(ColorPrintTest):
    def test_enable(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            config(enable=False)
            colorprint("Hello, World!", fg=FG_BLACK, bg=BG_RED)
            out = buf.getvalue()
        self.assertEqual(out, "Hello, World!\n")

        with io.StringIO() as buf, redirect_stdout(buf):
            config({"enable": False})
            colorprint("Hello, World!", fg=FG_BLACK, bg=BG_RED)
            out = buf.getvalue()
        self.assertEqual(out, "Hello, World!\n")

    def test_fg_bg(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            config(fg=FG_BLACK, bg=BG_RED)
            colorprint("Hello, World!")
            out = buf.getvalue()
        self.assertTrue(out.rstrip().endswith(RESET))
        self.assertIn("Hello, World!", out)
        self.assertIn(FG_BLACK, out)
        self.assertIn(BG_RED, out)

        with io.StringIO() as buf, redirect_stdout(buf):
            config({"fg": FG_BLACK, "bg": BG_RED})
            colorprint("Hello, World!")
            out = buf.getvalue()
        self.assertTrue(out.rstrip().endswith(RESET))
        self.assertIn("Hello, World!", out)
        self.assertIn(FG_BLACK, out)
        self.assertIn(BG_RED, out)
