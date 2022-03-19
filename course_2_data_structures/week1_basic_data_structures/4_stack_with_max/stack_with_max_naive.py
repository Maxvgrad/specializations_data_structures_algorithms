# python3
import sys


class StackWithMax:
    def __init__(self):
        self.__stack = []
        # self.sorted_list = SortedLinkedList()
        self.sorted_list = BinarySearchSortedList()

    def Push(self, a):
        self.__stack.append(a)
        self.sorted_list.add(a)
        # self.sorted_list.sort(reverse=True)

    def Pop(self):
        assert (len(self.__stack))
        val = self.__stack.pop()
        self.sorted_list.remove(val)

    def Max(self):
        assert (len(self.__stack))
        return self.sorted_list.elements[0]


class BinarySearchSortedList:

    def __init__(self) -> None:
        super().__init__()
        self.elements = []

    def add(self, element):
        number_of_elements = len(self.elements)
        if number_of_elements < 5:
            for i in range(number_of_elements):
                if element > self.elements[i]:
                    self.elements.insert(i, element)
                    return
            self.elements.append(element)
            return

        def take(element_, mid_index):
            if self.elements[mid_index] < element_:
                if mid_index == 0 or element_ <= self.elements[mid_index - 1]:
                    return True
            return False

        index = self.find_index(element, number_of_elements, take)
        if index == -1:
            index = number_of_elements
        self.elements.insert(index, element)

    def remove(self, element):
        number_of_elements = len(self.elements)
        if number_of_elements < 5:
            for i in range(number_of_elements):
                if element == self.elements[i]:
                    del self.elements[i]
                    return
            return

        def take(element_, mid_index):
            if self.elements[mid_index] == element_:
                return True

        index = self.find_index(element, number_of_elements, take)
        if index == -1:
            return
        del self.elements[index]

    def find_index(self, element, number_of_elements, take):
        left_pointer = 0
        right_pointer = number_of_elements-1

        while left_pointer <= right_pointer:
            mid_index = int(round((left_pointer + right_pointer) / 2, 0))

            if take(element, mid_index):
                return mid_index

            if element > self.elements[mid_index]:
                right_pointer = mid_index-1
            else:
                left_pointer = mid_index+1

        return -1

class SortedLinkedList:

    def __init__(self) -> None:
        super().__init__()
        self.root_item = None

    def add(self, val):

        def is_match(item):
            return item.next_item.val < val

        if self.root_item is None:
            self.root_item = Item(val, None)
            return
        else:
            if self.root_item.val < val:
                self.root_item = Item(val, self.root_item)
                return

            self.find_item_and_perform_action(
                    is_match,
                    lambda item: item.assign_new_next(Item(val, item.next_item)),
                    lambda item: (
                        item.assign_new_next(Item(val, item.next_item))
                    )
                )
            return

    def get(self, index=0):
        if self.root_item is None:
            return 0
        return self.root_item.val

    def remove(self, val):
        if self.root_item is None:
            return

        def is_match(item):
            return item.next_item is not None and item.next_item.val == val

        if self.root_item.val == val:
            self.root_item = self.root_item.next_item
            return

        self.find_item_and_perform_action(
            is_match,
            lambda item: item.assign_new_next(item.next_item.next_item),
            lambda item: ()
        )

    def find_item_and_perform_action(self, is_match, action, action_when_none_match):
        item = self.root_item
        while item.next_item is not None and not is_match(item):
            item = item.next_item

        if item.next_item is None:
            action_when_none_match(item)
        else:
            action(item)


class Item:

    def __init__(self, val, next_item) -> None:
        super().__init__()
        self.val = val
        self.next_item = next_item

    def assign_new_next(self, new_next):
        self.next_item = new_next


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert (0)
