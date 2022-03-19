# python3


def max_sliding_window_naive(sequence, m):
    maximums = []
    max_index = 0
    max_value = sequence[max_index]
    for i in range(1, m + 1):
        if i < len(sequence) and sequence[i] > max_value:
            max_value = sequence[i]
            max_index = i

    for i in range(0, len(sequence) - m + 1):
        if i > max_index:
            max_index = i
            max_value = sequence[max_index]
            for j in range(i+1, i + m):
                if j == len(sequence):
                    break
                if sequence[j] > max_value:
                    max_value = sequence[j]
                    max_index = j
        elif i+m < len(sequence) and max_value < sequence[i+m-1]:
            max_value = sequence[i+m-1]
            max_index = i+m-1

        maximums.append(max_value)

    return maximums


class LimitedSizeStack:

    def __init__(self, size) -> None:
        super().__init__()
        self.size = size
        self.stack = StackWithMax

    def Push(self, a):
        self.__stack.append(a)
        self.sorted_list.add(a)

    def Pop(self):
        assert (len(self.__stack))
        val = self.__stack.pop()
        self.sorted_list.remove(val)

    def Max(self):
        assert (len(self.__stack))
        return self.sorted_list.get(0)


class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.sorted_list = SortedLinkedList()
        self.size = 0

    def Push(self, a):
        self.__stack.append(a)
        self.sorted_list.add(a)
        self.size += 1

    def Pop(self):
        assert (len(self.__stack))
        self.size -= 1
        val = self.__stack.pop()
        self.sorted_list.remove(val)

    def Max(self):
        assert (len(self.__stack))
        return self.sorted_list.get(0)

    def Size(self):
        return self.size

class SortedLinkedList:

    def __init__(self) -> None:
        super().__init__()
        self.root_item = None

    def add(self, val):
        # item is the root
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
                    lambda item: item.assign_new_next(item.next_item.next_item),
                    lambda item: (
                        item.assign_new_next(Item(val, item.next_item))
                    )
                )
            return

    def get(self, index=0):
        return self.root_item.val

    def remove(self, val):
        is_match = lambda item, v=val: item.next_item is not None and item.next_item.val == v
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
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

