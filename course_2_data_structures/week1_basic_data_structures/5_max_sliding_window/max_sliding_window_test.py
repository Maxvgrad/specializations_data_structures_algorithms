from max_sliding_window import max_sliding_window_naive
import unittest
import random


class TestMaxSlidingWindow(unittest.TestCase):

    def test_sample(self):
        self.assertEqual([7, 7, 5, 6, 6], max_sliding_window_naive([2, 7, 3, 1, 5, 2, 6, 2], 4))
        self.assertEqual([1], max_sliding_window_naive([1], 1))
