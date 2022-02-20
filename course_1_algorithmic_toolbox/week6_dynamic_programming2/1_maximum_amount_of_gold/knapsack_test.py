from knapsack import optimal_weight, Step, Value
import unittest
import random
import timeout_decorator


class TestKnapsack(unittest.TestCase):

    def test_from_pdf(self):
        self.assertEqual(9, optimal_weight(10, [1, 4, 8]))
        self.assertEqual(10, optimal_weight(10, [1, 4, 8, 1]))

    def test_when_knapsack_is_too_small(self):
        self.assertEqual(0, optimal_weight(10, [300, 100]))

    def test_when_bricks_are_empty(self):
        self.assertEqual(0, optimal_weight(1, [0, 0]))

    @timeout_decorator.timeout(seconds=10)
    def test_when_knapsack_has_weight_1000_and_11_bricks(self):
        self.assertEqual(1000, optimal_weight(1000, [1, 2, 4, 8, 16, 32, 64, 128, 256, 516, 1024]))

    @timeout_decorator.timeout(seconds=10)
    def test_when_knapsack_has_weight_1000_and_12_bricks(self):
        self.assertEqual(1000, optimal_weight(1000, [1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 516, 1024]))

    @timeout_decorator.timeout(seconds=10)
    def test_when_knapsack_has_weight_1000_and_15_bricks(self):
        self.assertEqual(1000, optimal_weight(1000, [1, 1, 1, 1, 1, 1, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 32, 32, 32, 256, 516, 1024, 1024]))

    def test_list_not_equals(self):
        self.assertNotEquals([1, 2], [2, 1])

    def test_list_can_be_sorted_descending_order(self):
        list_to_sort = [1, 2, 100, 4, 0]
        list_to_sort.sort(reverse=True)
        self.assertEquals(list_to_sort, [100, 4, 2, 1, 0])

    def test_list_to_string_return_list_as_string(self):
        self.assertEquals(str([100, 4, 2, 1, 0]), "[100, 4, 2, 1, 0]")

    def test_set_equals(self):
        self.assertEqual({1, 2}, {2, 1})

    def test_step_contains_when_value_present_should_return_True(self):
        value_five = Value(5)
        value_one = Value(1)
        step = Step(value_five, Step(Value(3), Step(value_one, None)))
        self.assertTrue(step.contains(value_five), 'Current step value')
        self.assertTrue(step.contains(value_one), 'Root step value')

    def test_step_contains_when_value_missing_should_return_False(self):
        step = Step(Value(5), Step(Value(3), Step(Value(1), None)))
        self.assertFalse(step.contains(Value(6)))

    def test_step_contains_when_value_is_present_but_the_value_object_is_different_should_return_False(self):
        step = Step(Value(5), Step(Value(3), Step(Value(1), None)))
        self.assertFalse(step.contains(Value(5)))

    def test_should_return_total_value(self):
        step = Step(Value(5), Step(Value(3), Step(Value(1), None)))
        self.assertEqual(9, step.get_total_value().value)

    def test_when_step_is_root_should_return_its_value(self):
        step = Step(Value(1), None)
        self.assertEqual(1, step.get_total_value().value)

    def test_when_value_objects_have_same_content_should_not_be_equal(self):
        self.assertNotEquals(Value(5), Value(5))

    def test_when_value_equals_itself(self):
        val = Value(5)
        self.assertEquals(val, val)

    def test_value_object_supports_less_than_or_equals(self):
        self.assertTrue(Value(1) <= Value(5))
        self.assertTrue(Value(1) <= Value(1))
        self.assertFalse(Value(5) <= Value(1))

    def test_value_object_supports_less_than(self):
        self.assertTrue(Value(1) < Value(5))
        self.assertFalse(Value(1) < Value(1))
        self.assertFalse(Value(5) < Value(1))
