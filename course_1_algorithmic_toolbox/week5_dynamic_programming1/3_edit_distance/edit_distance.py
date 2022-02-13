# Uses python3
from typing import Type


def edit_distance(s, t):
    return edit_distance_dp(s, t)


MATCH = 'MATCH'
INSERT = 'INSERT'
DELETE = 'DELETE'


def edit_distance_recursive(s, t):
    def edit_distance_recursive_inner(i, j):
        if i == -1 and j == -1:
            return 0

        if i == -1 and j > -1:
            return j + 1

        if i > -1 and j == -1:
            return i + 1

        opt = {
            MATCH: edit_distance_recursive_inner(i - 1, j - 1) + match(s[i], t[j]),
            INSERT: edit_distance_recursive_inner(i, j - 1) + indel(t[j]),
            DELETE: edit_distance_recursive_inner(i - 1, j) + indel(s[i])
        }

        score_min = opt[MATCH]

        if score_min > opt[INSERT]:
            score_min = opt[INSERT]
        if score_min > opt[DELETE]:
            score_min = opt[DELETE]
        return score_min

    return edit_distance_recursive_inner(len(s) - 1, len(t) - 1)


def indel(a):
    return 1


def match(a, b):
    if a == b:
        return 0
    else:
        return 1


def edit_distance_dp(s, t):
    rows, cols = (len(t) + 1, len(s) + 1)
    matrix = [[0 for i in range(0, cols)] for j in range(0, rows)]

    for i in range(0, rows):
        for j in range(0, cols):

            if i == 0 and j == 0:
                matrix[i][j] = Node()
                continue

            col_elem = s[j - 1]
            row_elem = t[i - 1]

            if i == 0:
                parent = matrix[i][j - 1]
                matrix[i][j] = Node(parent.score + indel(col_elem), parent)
                continue

            if j == 0:
                parent = matrix[i - 1][j]
                matrix[i][j] = Node(parent.score + indel(row_elem), parent)
                continue

            score_insert_node_pair = get_pair(matrix[i - 1][j], lambda: indel(row_elem))
            score_delete_node_pair = get_pair(matrix[i][j - 1], lambda: indel(col_elem))
            score_match_mismatch_node_pair = get_pair(matrix[i - 1][j - 1], lambda: match(row_elem, col_elem))

            pairs_arr = [score_insert_node_pair, score_delete_node_pair, score_match_mismatch_node_pair]

            min_score = min([pair[0] for pair in pairs_arr])

            optimal_parent_nodes = [pair[1] for pair in pairs_arr if min_score == pair[0]]

            matrix[i][j] = Node(min_score, optimal_parent_nodes)

    return matrix[rows - 1][cols - 1].score


def get_min_score(pairs):
    return min([pair[0] for pair in pairs])


def get_pair(node, score_function):
    if type(node) is int:
        print('')
    return (node.score + score_function(), node)


class Node:

    def __init__(self, score=0, *roots) -> None:
        super().__init__()
        if roots is None:
            roots = []
        self.score = score
        self.roots = roots

    # def __str__(self) -> str:
    #     return 'Score: {}'.format(self.score)

if __name__ == "__main__":
    print(edit_distance(input(), input()))
