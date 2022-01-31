from change_dp import get_change
import unittest
import random


class TestMaxPairwiseProduct(unittest.TestCase):

    def test_get_change(self):
        self.assertEqual(2, get_change(2))
        self.assertEqual(1, get_change(3))
