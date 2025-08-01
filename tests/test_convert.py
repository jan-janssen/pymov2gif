import os
from pymov2gif import convert
from unittest import TestCase


class TestConvert(TestCase):
    def test_convert(self):
        input_file = os.path.join(os.path.dirname(__file__), "white.mov")
        convert(input_file, resolution='20x20', framerate=10, output_file=None)
        self.assertTrue(os.path.exists("white.gif"))

    def tearDown(self):
        if os.path.exists("white.gif"):
            os.remove("white.gif")