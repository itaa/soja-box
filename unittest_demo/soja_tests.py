import unittest
from soja_any_scale import Scale


class AnyScaleTest(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.scale = Scale()

    def tearDown(self):
        print('tearDown')
        self.scale = None

    def test_10_16_16(self):
        self.assertEqual('10', self.scale.any_scale(10, 16, 16))

    def test_7_21_10(self):
        self.assertEqual('15', self.scale.any_scale(7, 21, 10))

    def test_10_17_8(self):
        self.assertEqual('21', self.scale.any_scale(10, 17, 8))

    def test_10_88_18(self):
        self.assertEqual('4*16*', self.scale.any_scale(10, 88, 18))

    def test_10_85_18(self):
        self.assertEqual('4D', self.scale.any_scale(10, 85, 18))


if __name__ == "__main__":
    unittest.main()
