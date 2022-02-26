from check_brackets import find_mismatch
import unittest
import random


class TestFractionalKnapsack(unittest.TestCase):

    def test_when_match_should_return_success(self):
        self.assertEqual("Success", find_mismatch('(){}[]{([])}'))

    def test_when_string_do_not_have_open_bracket_should_return_index_of_closing_bracket(self):
        self.assertEqual(1, find_mismatch(']'))
        self.assertEqual(1, find_mismatch(')'))
        self.assertEqual(1, find_mismatch('}'))
        self.assertEqual(3, find_mismatch('()}'))
        self.assertEqual(3, find_mismatch('())'))
        self.assertEqual(3, find_mismatch('()]'))

    def test_when_closing_bracket_do_not_match_open_bracket_should_return_index_of_closing_bracket(self):
        self.assertEqual(2, find_mismatch('{]'))
        self.assertEqual(2, find_mismatch('[)'))
        self.assertEqual(2, find_mismatch('[}'))

    def test_when_open_bracket_does_not_have_closing_bracket_should_return_index_of_open_bracket(self):
        self.assertEqual(1, find_mismatch('([]'))
        self.assertEqual(1, find_mismatch('{[]'))
        self.assertEqual(1, find_mismatch('[[]'))
