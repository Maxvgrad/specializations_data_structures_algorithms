from binary_search import binary_search, binary_search_naive
import unittest


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(2, binary_search_naive([1, 5, 8, 12, 13], 8))
        self.assertEqual(0, binary_search_naive([1, 5, 8, 12, 13], 1))
        self.assertEqual(-1, binary_search_naive([1, 5, 8, 12, 13], 23))

        # 5
        # 1 5 8 12 13
        # 5
        # 8 1 23 1 11
        self.assertEqual(2, binary_search([1, 5, 8, 12, 13], 8))
        self.assertEqual(0, binary_search([1, 5, 8, 12, 13], 1))
        self.assertEqual(4, binary_search([1, 5, 8, 12, 13], 13))
        self.assertEqual(-1, binary_search([1, 5, 8, 12, 13], 15))
        self.assertEqual(-1, binary_search([1, 5, 8, 12, 13], 0))
        self.assertEqual(-1, binary_search([1, 5, 8, 12, 13], 7))
