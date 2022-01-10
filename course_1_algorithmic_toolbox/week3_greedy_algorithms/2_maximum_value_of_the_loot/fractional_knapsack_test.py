from fractional_knapsack import get_optimal_value
import unittest
import random


class TestFractionalKnapsack(unittest.TestCase):

    def test_get_optimal_value(self):
        self.assertEqual(180, get_optimal_value(50, [20, 50, 30], [60, 100, 120]))
        self.assertEqual(500, get_optimal_value(1000, [30], [500]))
        self.assertEqual(166.667, get_optimal_value(10, [30], [500]))

