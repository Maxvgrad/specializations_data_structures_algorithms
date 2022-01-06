from gcd import gcd, gcd_naive
import unittest


class TestGcd(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(7, gcd_naive(7, 21))
        self.assertEqual(11, gcd_naive(121, 22))
        self.assertEqual(3, gcd_naive(357, 234))
        self.assertEqual(3, gcd(357, 234))
        # self.assertEqual(3, gcd(7))
