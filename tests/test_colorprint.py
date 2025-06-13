# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/Yzi-Li/pcolory/blob/main/copyright.txt


import unittest
import io
from contextlib import redirect_stdout

from pcolory import colorprint
from pcolory.colors import FG_BLACK, BG_RED, RESET


class TestColorPrint(unittest.TestCase):
    def test_colorprint(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello, World", fg=FG_BLACK, bg=BG_RED)
            out = buf.getvalue()
        self.assertIn(FG_BLACK, out)
        self.assertIn(BG_RED, out)
        self.assertIn("Hello, World", out)
        self.assertTrue(out.rstrip().endswith(RESET))

    def test_multiple(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello,", "World!", fg=FG_BLACK, bg=BG_RED)
            out = buf.getvalue()
        self.assertIn("Hello,", out)
        self.assertIn("World!", out)
        self.assertIn(FG_BLACK, out)
        self.assertIn(BG_RED, out)

    def test_sep_end(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            colorprint("Hello", "World", fg=FG_BLACK, bg=BG_RED, sep=", ", end="!")
            out = buf.getvalue()
        self.assertTrue(out.rstrip().endswith(RESET))
        self.assertIn("Hello, World!", out)
        self.assertIn(FG_BLACK, out)
        self.assertIn(BG_RED, out)
