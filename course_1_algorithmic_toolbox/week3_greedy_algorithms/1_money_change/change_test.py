from change import get_change
import unittest
import random


class TestChange(unittest.TestCase):

    def test_max_pairwise(self):
        self.assertEqual(6, get_change(28))

