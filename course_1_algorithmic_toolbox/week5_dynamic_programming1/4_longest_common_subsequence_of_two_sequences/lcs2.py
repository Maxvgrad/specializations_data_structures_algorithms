#Uses python3

import sys


def lcs2_naive_v0(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0

    arr_long = b
    arr_short = a
    if len(a) > len(b):
        arr_long = a
        arr_short = b

    sequence_max = 0

    for start_index in range(len(arr_long)):
        arr_long_pointer = start_index
        sequence = 0
        arr_short_last_match_index = 0
        while arr_long_pointer < len(arr_long):
            arr_short_pointer = arr_short_last_match_index
            while arr_short_pointer < len(arr_short):
                if arr_long[arr_long_pointer] == arr_short[arr_short_pointer]:
                    arr_short_last_match_index = arr_short_pointer + 1
                    sequence += 1
                    break
                arr_short_pointer += 1

            arr_long_pointer += 1

        if sequence > sequence_max:
            sequence_max = sequence

    return sequence_max


def lcs2_naive(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0

    elem_indexes_dic_a = init_dic(a)
    elem_indexes_dic_b = init_dic(b)

    pointer_a = 0
    pointer_b = 0
    sequence = 0
    while pointer_a < len(a) and pointer_b < len(b):
        elem_a = a[pointer_a]
        elem_b = b[pointer_b]

        if elem_a == elem_b:
            pointer_a += 1
            pointer_b += 1
            sequence += 1
            continue

        elem_a_indexes_in_arr_b = find_element_indexes_after_pointer(pointer_b, elem_a, elem_indexes_dic_b)
        elem_b_indexes_in_arr_a = find_element_indexes_after_pointer(pointer_a, elem_b, elem_indexes_dic_a)

        if len(elem_a_indexes_in_arr_b) == 0 and len(elem_b_indexes_in_arr_a) == 0:
            pointer_a += 1
            pointer_b += 1
            continue
        elif len(elem_a_indexes_in_arr_b) == 0:
            pointer_a += 1
            continue
        elif len(elem_b_indexes_in_arr_a) == 0:
            pointer_b += 1
            continue

        elem_a_index_in_b = elem_a_indexes_in_arr_b[0]
        elem_b_index_in_a = elem_b_indexes_in_arr_a[0]

        elem_a_indexes_in_arr_a = find_element_indexes_after_pointer(pointer_a, elem_a, elem_indexes_dic_a)
        elem_b_indexes_in_arr_b = find_element_indexes_after_pointer(pointer_b, elem_b, elem_indexes_dic_b)
        if len(elem_a_indexes_in_arr_a) == 0 and len(elem_b_indexes_in_arr_b) == 0:
            if elem_a_index_in_b <= elem_b_index_in_a:
                pointer_b += 1
            else:
                pointer_a += 1
        elif len(elem_b_indexes_in_arr_b) == 0:
            if elem_b_index_in_a < elem_a_indexes_in_arr_a[0]:
                pointer_a += 1
            else:
                pointer_b += 1
        elif len(elem_a_indexes_in_arr_a) == 0:
            if elem_a_index_in_b < elem_b_indexes_in_arr_b[0]:
                pointer_b += 1
            else:
                pointer_a += 1
        else:
            if elem_a_index_in_b < elem_b_index_in_a:
                pointer_b += 1
            else:
                pointer_a += 1

    return sequence


def init_dic(arr):
    element_indexes_dic = {}
    for i in range(len(arr)):
        elem = arr[i]
        if elem not in element_indexes_dic:
            element_indexes_dic[elem] = []

        element_indexes_dic[elem].append(i)
    return element_indexes_dic


def find_element_indexes_after_pointer(pointer, element, element_indexes_dic):
    indexes = []
    if element in element_indexes_dic:
        indexes = element_indexes_dic[element]
    return get_indexes_greater_than_pointer(pointer, indexes)


def get_indexes_greater_than_pointer(pointer, indexes):
    for i in range(len(indexes)):
        if indexes[i] > pointer:
            return indexes[i:]
    return []


def init_matrix(s, t):
    rows, cols = (len(t) + 1, len(s) + 1)
    matrix = [[0 for _ in range(0, cols)] for _ in range(0, rows)]

    for i in range(0, rows):
        for j in range(0, cols):

            if i == 0 and j == 0:
                matrix[i][j] = Node()
                continue

            if i == 0:
                parent = matrix[i][j - 1]
                matrix[i][j] = Node(None, parent.score + indel(None), parent)
                continue

            if j == 0:
                parent = matrix[i - 1][j]
                matrix[i][j] = Node(None, parent.score + indel(None), parent)
                continue

            col_elem = s[j - 1]
            row_elem = t[i - 1]

            if col_elem == row_elem:
                parent = matrix[i - 1][j-1]
                matrix[i][j] = Node(col_elem, parent.score + match(col_elem, row_elem), parent)
                continue

            score_insert_node_pair = get_pair(matrix[i - 1][j], lambda: indel(row_elem))
            score_delete_node_pair = get_pair(matrix[i][j - 1], lambda: indel(col_elem))

            pairs_arr = [score_insert_node_pair, score_delete_node_pair]

            max_score = max([pair[0] for pair in pairs_arr])

            optimal_parent_nodes = [pair[1] for pair in pairs_arr if max_score == pair[0]]

            matrix[i][j] = Node(None, max_score, optimal_parent_nodes[0])

    return matrix


def lcs2(s, t):
    return init_matrix(s, t)[len(t)][len(s)].score


def get_min_score(pairs):
    return min([pair[0] for pair in pairs])


def get_pair(node, score_function):
    if type(node) is int:
        print('')
    return (node.score + score_function(), node)


def indel(a):
    return 0


def match(a, b):
    if a == b:
        return 1
    else:
        raise Exception('Unsupported')


class Node:

    def __init__(self, elem=None, score=0, root=None) -> None:
        super().__init__()
        self.elem = elem
        self.score = score
        self.root = root

    def is_root(self):
        return self.root is None

    def is_match(self):
        return self.elem is None

    def __str__(self) -> str:
        return 'Score: {}'.format(self.score)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
