from edit_distance import edit_distance_recursive, edit_distance, get_min_score
import unittest
import random


class TestEditDistance(unittest.TestCase):

    def test_edit_distance_cases_from_book(self):
        self.assertEqual(3, edit_distance('short', 'ports'))
        self.assertEqual(0, edit_distance('ab', 'ab'))
        self.assertEqual(5, edit_distance('editing', 'distance'))

    def test_get_min_score(self):
        self.assertEqual(0, get_min_score([(1, None), (0, None), (1, None)]))
        self.assertEqual(0, get_min_score([(2, None), (0, None), (1, None)]))
        self.assertEqual(0, get_min_score([(0, None), (0, None), (0, None)]))
