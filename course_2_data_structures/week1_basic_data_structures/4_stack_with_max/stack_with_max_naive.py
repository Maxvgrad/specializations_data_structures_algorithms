# python3
import sys


class StackWithMax:
    def __init__(self):
        self.__stack = []
        # self.sorted_list = SortedLinkedList()
        self.sorted_list = []

    def Push(self, a):
        self.__stack.append(a)
        self.sorted_list.append(a)
        self.sorted_list.sort(reverse=True)

    def Pop(self):
        assert (len(self.__stack))
        val = self.__stack.pop()
        self.sorted_list.remove(val)

    def Max(self):
        assert (len(self.__stack))
        return self.sorted_list[0]


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
