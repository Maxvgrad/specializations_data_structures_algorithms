from stack_with_max_naive import StackWithMax
import unittest


class TestMaxSlidingWindow(unittest.TestCase):

    def test_should_return_correct_max(self):
        stack = StackWithMax()
        stack.Push(2)
        stack.Push(1)
        self.assertEqual(2, stack.Max())

    def test_when_pop_max_should_return_correct_max(self):
        stack = StackWithMax()
        stack.Push(1)
        stack.Push(2)
        stack.Pop()
        self.assertEqual(1, stack.Max())

    def test_when_pop_max_should_return_correct_max(self):
        stack = StackWithMax()
        stack.Push(1)
        stack.Push(2)
        self.assertEqual(2, stack.Max())
        stack.Pop()
        self.assertEqual(1, stack.Max())



    # def test_when_pop_on_empty_stack_should_not_fail(self):
    #     stack = StackWithMax()
    #     stack.Pop()
    #     self.assertTrue(True)
    #Failed case #10/60: (Wrong answer)
    def test_case_10(self):
        stack = StackWithMax()
        stack.Push(0)
        self.assertEqual(0, stack.Max())
        stack.Push(1)
        self.assertEqual(1, stack.Max())
        stack.Push(2)
        self.assertEqual(2, stack.Max())
        stack.Push(3)
        self.assertEqual(3, stack.Max())
        stack.Push(4)
        self.assertEqual(4, stack.Max())
        stack.Push(5)
        self.assertEqual(5, stack.Max())
        stack.Push(4)
        self.assertEqual(5, stack.Max())
        stack.Push(3)
        self.assertEqual(5, stack.Max())
        stack.Push(2)
        self.assertEqual(5, stack.Max())
        stack.Push(1)
        self.assertEqual(5, stack.Max())

        stack.Pop()
        self.assertEqual(5, stack.Max())
        stack.Pop()
        self.assertEqual(5, stack.Max())
        stack.Pop()
        self.assertEqual(5, stack.Max())
        stack.Pop()
        self.assertEqual(5, stack.Max())

        stack.Pop()
        self.assertEqual(4, stack.Max(), 'after pop')
        stack.Pop()
        self.assertEqual(3, stack.Max())
        stack.Pop()
        self.assertEqual(2, stack.Max())
        stack.Pop()
        self.assertEqual(1, stack.Max())
        stack.Pop()
        self.assertEqual(0, stack.Max())
