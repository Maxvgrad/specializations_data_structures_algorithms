from partition3 import partition3, partition3_recursion
import unittest


class TestKnapsack(unittest.TestCase):

    def test_when_array_sum_divided_by_3_is_float_return_0(self):
        self.assertEqual(0, partition3([3, 3, 3, 4]))

    def test_when_array_sum_divided_by_3_is_float_return_0_recursive(self):
        self.assertEqual(0, partition3_recursion([3, 3, 3, 4]))

    def test_when_array_sum_divided_by_3_but_can_not_be_partitioned_return_0(self):
        self.assertEqual(0, partition3([3, 3, 3, 3]))

    def test_when_array_sum_divided_by_3_but_can_not_be_partitioned_return_0_recursive(self):
        self.assertEqual(0, partition3_recursion([3, 3, 3, 3]))

    def test_when_array_has_one_value_return_0(self):
        self.assertEqual(0, partition3([3]))

    def test_when_array_has_one_value_return_0_recursive(self):
        self.assertEqual(0, partition3_recursion([3]))

    def test_when_possible_to_partition_should_return_1_case_0(self):
        self.assertEqual(1, partition3([3, 3, 3]))
        self.assertEqual(1, partition3([1, 1, 1]))

    def test_when_possible_to_partition_should_return_1_case_0_recursive(self):
        self.assertEqual(1, partition3_recursion([3, 3, 3]))
        self.assertEqual(1, partition3_recursion([1, 1, 1]))

    def test_when_possible_to_partition_should_return_1_case_1(self):
        self.assertEqual(1, partition3([3, 3, 2, 1]))

    def test_when_possible_to_partition_should_return_1_case_1_recursive(self):
        self.assertEqual(1, partition3_recursion([3, 3, 2, 1]))

    def test_when_possible_to_partition_should_return_1_case_2(self):
        self.assertEqual(1, partition3([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]))
        self.assertEqual(1, partition3([1, 117, 118, 118]))
        self.assertEqual(1, partition3([1, 117, 59, 59, 118]))
        self.assertEqual(1, partition3([1, 117, 59, 59, 59, 1, 58]))
        self.assertEqual(1, partition3([1, 117, 59, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3([1, 1, 116, 59, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3([1, 1, 1, 5, 55, 55, 1, 58, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3([1, 1, 1, 5, 55, 55, 1, 29, 29, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3([1, 1, 1, 5, 55, 55, 1, 29, 1, 14, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3([1, 1, 1, 5, 55, 55, 1, 29, 1, 7, 7, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3([1, 1, 1, 5, 55, 55, 1, 29, 1, 7, 3, 4, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3([1, 1, 1, 5, 55, 50, 5, 1, 29, 1, 7, 3, 4, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3([1, 1, 1, 5, 55, 25, 25, 2, 3, 1, 29, 1, 7, 3, 4, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3([1, 1, 1, 5, 55, 25, 5, 20, 2, 3, 1, 29, 1, 7, 3, 4, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3([1, 1, 1, 5, 55, 25, 5, 10, 10, 2, 3, 1, 29, 1, 7, 3, 4, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3([1, 1, 1, 5, 55, 25, 5, 10, 5, 5, 2, 3, 1, 29, 1, 7, 3, 4, 14, 59, 59, 1, 29, 29]))

    def test_when_possible_to_partition_should_return_1_case_2_recursion(self):
        self.assertEqual(1, partition3_recursion([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]))
        self.assertEqual(1, partition3_recursion([1, 117, 118, 118]))
        self.assertEqual(1, partition3_recursion([1, 117, 59, 59, 118]))
        self.assertEqual(1, partition3_recursion([1, 117, 59, 59, 59, 1, 58]))
        self.assertEqual(1, partition3_recursion([1, 117, 59, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3_recursion([1, 1, 116, 59, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3_recursion([1, 1, 1, 5, 55, 55, 1, 58, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3_recursion([1, 1, 1, 5, 55, 55, 1, 29, 29, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3_recursion([1, 1, 1, 5, 55, 55, 1, 29, 1, 14, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3_recursion([1, 1, 1, 5, 55, 55, 1, 29, 1, 7, 7, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3_recursion([1, 1, 1, 5, 55, 55, 1, 29, 1, 7, 3, 4, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3_recursion([1, 1, 1, 5, 55, 50, 5, 1, 29, 1, 7, 3, 4, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3_recursion([1, 1, 1, 5, 55, 25, 25, 2, 3, 1, 29, 1, 7, 3, 4, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3_recursion([1, 1, 1, 5, 55, 25, 5, 20, 2, 3, 1, 29, 1, 7, 3, 4, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3_recursion([1, 1, 1, 5, 55, 25, 5, 10, 10, 2, 3, 1, 29, 1, 7, 3, 4, 14, 59, 59, 1, 29, 29]))
        self.assertEqual(1, partition3_recursion([1, 1, 1, 5, 55, 25, 5, 10, 5, 5, 2, 3, 1, 29, 1, 7, 3, 4, 14, 59, 59, 1, 29, 29]))
