import unittest
from soja_any_scale import Scale


class AnyScaleTest(unittest.TestCase):
    def setUp(self):
        self.scale = Scale()

    def tearDown(self):
        self.scale = None

    def test_10_16_16(self):
        self.assertEquals('10', self.scale.any_scale(10, 16, 16))

    def test_8_19_10(self):
        self.assertEquals('17', self.scale.any_scale(8, 19, 10))

    def test_10_17_8(self):
        self.assertEquals('19', self.scale.any_scale(10, 17, 8))
