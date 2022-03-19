from stack_with_max_naive import StackWithMax, BinarySearchSortedList
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

    def test_when_pop_max_should_return_correct_max_2(self):
        stack = StackWithMax()
        stack.Push(1)
        stack.Push(2)
        self.assertEqual(2, stack.Max())
        stack.Pop()
        self.assertEqual(1, stack.Max())

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

    # Failed
    # case  # 11/60: (Wrong answer)
    def test_case_11(self):

        stack = StackWithMax()
        stack.Push(15560)
        self.assertEqual(15560, stack.Max())
        stack.Push(25104)
        self.assertEqual(25104, stack.Max())
        stack.Push(93136)
        self.assertEqual(93136, stack.Max())
        stack.Push(19637)
        self.assertEqual(93136, stack.Max())
        stack.Push(54647)
        self.assertEqual(93136, stack.Max())
        stack.Push(13521)
        self.assertEqual(93136, stack.Max())
        stack.Push(57160)
        self.assertEqual(93136, stack.Max())
        stack.Push(8087)
        self.assertEqual(93136, stack.Max())
        stack.Push(48207)
        self.assertEqual(93136, stack.Max())
        stack.Push(53519)
        self.assertEqual(93136, stack.Max())

        stack.Pop()
        self.assertEqual(93136, stack.Max())
        stack.Pop()
        self.assertEqual(93136, stack.Max())
        stack.Pop()
        self.assertEqual(93136, stack.Max())
        stack.Pop()
        self.assertEqual(93136, stack.Max())
        stack.Pop()
        self.assertEqual(93136, stack.Max())
        stack.Pop()
        self.assertEqual(93136, stack.Max())
        stack.Pop()
        self.assertEqual(93136, stack.Max())
        stack.Pop()
        self.assertEqual(25104, stack.Max())
        stack.Pop()
        self.assertEqual(15560, stack.Max())

    def test_binary_sorted_list_when_empty_should_append(self):
        list = BinarySearchSortedList()
        list.add(10)
        self.assertEqual([10], list.elements)

    def test_binary_sorted_list_when_one_element_gt_all_elements_in_list_add_to_zero_index(self):
        list = BinarySearchSortedList()
        list.add(10)
        list.add(20)
        self.assertEqual([20, 10], list.elements)

    def test_binary_sorted_list_when_small_size_should_add_in_the_end(self):
        list = BinarySearchSortedList()
        list.add(20)
        list.add(10)
        self.assertEqual([20, 10], list.elements)

    def test_binary_sorted_list_when_small_size_should_add_in_the_middle(self):
        list = BinarySearchSortedList()
        list.add(10)
        list.add(20)
        list.add(15)
        self.assertEqual([20, 15, 10], list.elements)

    def test_binary_sorted_list_when_big_size_list_should_add_in_first(self):
        list = BinarySearchSortedList()

        for i in range(1, 11, 2): #1,3,5,7,9
            list.add(i)
        list.add(11)
        arr = [1, 3, 5, 7, 9, 11]
        arr.reverse()
        self.assertEqual(arr, list.elements)


    def test_binary_sorted_list_when_big_size_list_should_add_in_the_middle(self):
        list = BinarySearchSortedList()

        for i in range(1, 12, 2): #1,3,5,7,9,11
            list.add(i)
        list.add(8)
        arr = [1, 3, 5, 7, 8, 9, 11]
        arr.reverse()
        self.assertEqual(arr, list.elements)

    def test_binary_sorted_list_when_big_size_list_should_add_in_the_end(self):
        list = BinarySearchSortedList()
        for i in range(1, 12, 2): #1,3,5,7,9,11
            list.add(i)
        list.add(-3)
        arr = [-3, 1, 3, 5, 7, 9, 11]
        arr.reverse()
        self.assertEqual(arr, list.elements)


    def test_binary_sorted_list_should_first_element(self):
        list = BinarySearchSortedList()
        for i in range(1, 12, 2): #1,3,5,7,9,11
            list.add(i)
        list.remove(11)
        arr = [1, 3, 5, 7, 9]
        arr.reverse()
        self.assertEqual(arr, list.elements)

    def test_binary_sorted_list_should_remove_middle_element(self):
        list = BinarySearchSortedList()
        for i in range(1, 12, 2): #1,3,5,7,9,11
            list.add(i)
        list.remove(5)
        arr = [1, 3, 7, 9, 11]
        arr.reverse()
        self.assertEqual(arr, list.elements)

    def test_binary_sorted_list_should_last_element(self):
        list = BinarySearchSortedList()
        for i in range(1, 12, 2): #1,3,5,7,9,11
            list.add(i)
        list.remove(1)
        arr = [3, 5, 7, 9, 11]
        arr.reverse()
        self.assertEqual(arr, list.elements)
