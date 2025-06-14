import unittest

from pcolory import config


class ColorPrintTest(unittest.TestCase):
    def setUp(self):
        config({"enable": True, "fg": "", "bg": ""})
