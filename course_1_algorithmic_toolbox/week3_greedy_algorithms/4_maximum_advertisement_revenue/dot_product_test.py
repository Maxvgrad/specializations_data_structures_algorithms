from dot_product import max_dot_product
import unittest


class TestMaxDotProduct(unittest.TestCase):

    def test_max_dot_product(self):
        # a_positive_total max positive advertisements
        # b_positive_total max positive advertisements
        # N * (aPositive_n, bPositiveN)

        #


        # case
        self.assertEqual(100, max_dot_product([4, 2, 1], [20, 10, 0]))
        self.assertEqual(100, max_dot_product([2, 4, 1], [10, 20, 0]))
        self.assertEqual(100, max_dot_product([4, 2, -1], [20, 10, 0]))
        self.assertEqual(110, max_dot_product([4, 2, -1], [20, 10, -10]))
        self.assertEqual(105, max_dot_product([4, 2, 1, -1], [20, 10, -5, -10]))
        self.assertEqual(105, max_dot_product([4, -1, 2, 1], [20, 10, -5, -10]))

        self.assertEqual(60, max_dot_product([-4, -1, -2, -8], [20, 10, -5, -10]))
        # self.assertEqual(100, max_dot_product([4, 2, -1], [20, 10, 0]))


        # self.assertEqual(100, max_dot_product([-4, -2, -1], [20, 10, 0]))

        # case
        # -20 * -4 + -2 * 0 + -1 * 10
        # self.assertEqual(70, max_dot_product([-4, -2, -1], [10, 0, -20]))

