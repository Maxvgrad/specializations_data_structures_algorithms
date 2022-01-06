from lcm import lcm, lcm_naive
import unittest


class TestGcd(unittest.TestCase):

    def test_lcm(self):
        self.assertEqual(24, lcm_naive(6, 8))
        self.assertEqual(24, lcm(6, 8))
        self.assertEqual(12, lcm_naive(6, 12))
        self.assertEqual(12, lcm(6, 12))
