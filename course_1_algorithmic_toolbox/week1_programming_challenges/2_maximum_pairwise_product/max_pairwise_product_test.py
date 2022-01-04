from max_pairwise_product import max_pairwise_product
import unittest


class TestMaxPairwiseProduct(unittest.TestCase):

    def test_max_pairwise(self):
        self.assertEqual(60, max_pairwise_product([3, 5, 6, 10]))

    def test_max_pairwise_2(self):
        self.assertEqual(6, max_pairwise_product([1, 2, 3]))

    def test_max_pairwise_3(self):
        self.assertEqual(2, max_pairwise_product([1, 2]))
        self.assertEqual(2, max_pairwise_product([2, 1]))
