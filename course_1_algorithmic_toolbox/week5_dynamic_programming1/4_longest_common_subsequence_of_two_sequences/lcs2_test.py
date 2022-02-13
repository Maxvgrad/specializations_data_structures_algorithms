from lcs2 import lcs2, get_indexes_greater_than_pointer
import unittest
import random


class TestLongestCommonSubsequence(unittest.TestCase):

    def test_cases_from_pdf_naive(self):
        self.assertEqual(2, lcs2([2, 7, 5], [2, 5]), '[2, 7, 5], [2, 5]')
        self.assertEqual(0, lcs2([7], [1, 2, 3, 4]), '[7], [1, 2, 3, 4]')
        self.assertEqual(2, lcs2([2, 7, 8, 3], [5, 2, 8, 7]))

    def test_edge_cases(self):
        self.assertEqual(0, lcs2([], [1, 2, 3, 4]))
        self.assertEqual(0, lcs2([1, 2, 3, 4], []))
        self.assertEqual(0, lcs2([], []))

    def test_zero_sequence(self):
        self.assertEqual(0, lcs2([7], [1, 2, 3, 4]))
        self.assertEqual(0, lcs2([1, 2, 3, 4], [7]))

    def test_sequential_subsequent(self):
        self.assertEqual(4, lcs2([1, 2, 3, 4], [1, 2, 3, 4]))

    def test_sequential_subsequent_different_arrays_size(self):
        self.assertEqual(4, lcs2([1, 2, 3, 4], [1, 2, 3, 4, 5, 6]))
        self.assertEqual(4, lcs2([1, 2, 3, 4, 5, 6], [1, 2, 3, 4]))

    def test_sequential_subsequent_with_different_starting_points(self):
        self.assertEqual(4, lcs2([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))

    def test_one_inversion(self):
        self.assertEqual(3, lcs2([1, 2, 4, 3], [1, 2, 3, 4]))

    # def test_one_inversion_2(self):
    #     self.assertEqual(3, lcs2([1, 3, 4, 2, 3, 2, 3],  [1, 2, 3]))
    #     self.assertEqual(1, lcs2([3, 4],  [2, 3]))
    #     self.assertEqual(3, lcs2([3, 4],  [2, 3]))

    def test_match(self):
        self.assertEqual(1, lcs2([3, 4],  [3, 5]))

    def test_mismatch_present_miss(self):
        self.assertEqual(1, lcs2([3, 4],  [6, 3]))
        self.assertEqual(1, lcs2([5, 6],  [6, 3]))

    def test_mismatch_miss_miss(self):
        self.assertEqual(1, lcs2([5, 3],  [6, 3]))

    def test_mismatch_present_present(self):
        self.assertEqual(1, lcs2([5, 6],  [6, 5]))
        self.assertEqual(1, lcs2([5, 4, 6],  [6, 5]))

    def test_mismatch_present_present_duplicates_in_one_array(self):
        self.assertEqual(2, lcs2([2, 4, 6, 3, 2],  [3, 2]))

        self.assertEqual(2, lcs2([3, 2], [2, 4, 6, 3, 2]))

    def test_mismatch_present_present_duplicates_in_two_arrays(self):
        self.assertEqual(2, lcs2([3, 2, 9, 3], [2, 4, 2, 7, 3]))

    # Brainstorm cases
    def test_generate_cases(self):
        arr_len = 10
        arr_a = []
        arr_b = []
        for i in range(arr_len*2):
            elem = random.randint(1, 4)
            if i < arr_len:
                arr_a.append(elem)
            else:
                arr_b.append(elem)

        print('self.assertEqual(2, lcs2({}, {}))'.format(str(arr_a), str(arr_b)))

        self.assertEqual(3, lcs2([3, 1, 1, 2, 1], [3, 1, 1, 3, 3]), '[3, 1, 1, 2, 1] [3, 1, 1, 3, 3]')
        self.assertEqual(3, lcs2([2, 3, 3, 2, 1],
                                       [3, 3, 3, 2, 2]), '[2, 3, 3, 2, 1] [3, 3, 3, 2, 2]')
        self.assertEqual(2, lcs2([2, 1, 2, 1, 3],
                                       [3, 3, 3, 2, 2]), '[2, 1, 2, 1, 3] [3, 2, 2, 3, 1]')

        self.assertEqual(2, lcs2([2, 1, 2, 1, 3], [3, 9, 9, 2, 2]), '[2, 1, 2, 1, 3] [3, 2, 2, 3, 1]')

        self.assertEqual(2, lcs2([1, 3, 2, 1, 2], [2, 3, 2, 3, 3]), '[1, 3, 2, 1, 2] [2, 3, 2, 3, 3]')
        self.assertEqual(1, lcs2([3, 3, 2, 2, 3], [3, 1, 1, 1, 1]))
        self.assertEqual(4, lcs2([2, 3, 2, 2, 2], [2, 2, 2, 2, 3]))
        self.assertEqual(4, lcs2([2, 3, 3, 2, 1], [2, 3, 3, 1, 1]))
        self.assertEqual(3, lcs2([2, 1, 1, 2, 2], [3, 1, 2, 1, 2]))
        self.assertEqual(2, lcs2([3, 1, 1, 2, 3], [2, 2, 1, 2, 2]))
        self.assertEqual(3, lcs2([1, 2, 1, 3, 3], [1, 2, 3, 1, 1]))
        self.assertEqual(3, lcs2([2, 1, 3, 1, 2], [1, 3, 3, 2, 1]))

        self.assertEqual(3, lcs2([2, 4, 1, 4, 1], [1, 4, 3, 1, 2]))

        self.assertEqual(2, lcs2([1, 4, 2, 1, 4], [4, 4, 4, 4, 1]))
        self.assertEqual(2, lcs2([2, 4, 4, 3, 4], [3, 1, 4, 4, 2]))
        self.assertEqual(5, lcs2([4, 2, 4, 3, 4, 4, 4, 1, 1, 3], [4, 1, 3, 1, 3, 4, 2, 4, 4, 2]))

        arr_a: [1, 1, 2, 2, 1]
        arr_b: [3, 2, 3, 1, 1]
        self.assertEqual(2, lcs2([2, 1, 2, 1, 3], [3, 3, 3, 2, 2]), '[2, 1, 2, 1, 3] [3, 2, 2, 3, 1]')

    # Utils
    def test_find_element_indexes_after_pointer(self):
        self.assertEqual([5], get_indexes_greater_than_pointer(1, [5]))
