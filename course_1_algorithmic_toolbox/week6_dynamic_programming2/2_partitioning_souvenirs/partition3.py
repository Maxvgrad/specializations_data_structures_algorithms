# Uses python3
import sys
import itertools


def partition3(A):
    return partition3_recursion(A)


def partition3_dp(souvenirs):
    value_total = sum(souvenirs)

    if value_total % 3 != 0:
        return 0

    value_per_partition_total = value_total // 3

    # print('partition total: {}'.format(value_per_partition_total))

    def partition3_dp_inner(souvenirs, depth):

        matrix = [[0 for j in range(0, value_per_partition_total + 1)] for i in range(0, len(souvenirs) + 1)]

        for row_souvenir_index in range(1, len(souvenirs) + 1):
            for column_value_per_partition in range(1, value_per_partition_total + 1):
                matrix[row_souvenir_index][column_value_per_partition] = matrix[row_souvenir_index - 1][
                    column_value_per_partition]

                souvenir_value = souvenirs[row_souvenir_index - 1]
                if souvenir_value <= column_value_per_partition:
                    value = matrix[row_souvenir_index - 1][
                                column_value_per_partition - souvenirs[row_souvenir_index - 1]] + souvenir_value

                    if matrix[row_souvenir_index][column_value_per_partition] < value:
                        matrix[row_souvenir_index][column_value_per_partition] = value
            if matrix[row_souvenir_index][value_per_partition_total] == value_per_partition_total:
                if depth == 3:
                    return 1
                else:

                    # print('--')
                    # for i in range(-1, row_souvenir_index+1):
                    #     s_val = '0'
                    #     if i > 0:
                    #         s_val = str(souvenirs[i-1])
                    #
                    #     row_str = s_val + '\t: ['
                    #     if i == -1:
                    #         for index in range(0, value_per_partition_total+1):
                    #             row_str += str(index) + '\t'
                    #
                    #     else:
                    #         for element in matrix[i]:
                    #             row_str += str(element) + '\t'
                    #     row_str += ']'
                    #     print(row_str)
                    # print('--')

                    souvenir_indexes = []
                    row_pointer = row_souvenir_index  # + 1
                    column_pointer = value_per_partition_total  # + 1
                    while row_pointer > 0 and column_pointer > 0:
                        current_value = matrix[row_pointer][column_pointer]
                        while column_pointer > 0 and matrix[row_pointer][column_pointer - 1] == current_value:
                            column_pointer -= 1

                        while row_pointer > 0 and matrix[row_pointer - 1][column_pointer] == current_value:
                            row_pointer -= 1

                        row_pointer -= 1
                        souvenir_indexes.append(row_pointer)

                        column_pointer = column_pointer - souvenirs[row_pointer]
                    # print([souvenirs[i] for i in range(0, len(souvenirs)) if i in souvenir_indexes])
                    return partition3_dp_inner(
                        [souvenirs[i] for i in range(0, len(souvenirs)) if i not in souvenir_indexes], depth + 1)

        return 0

    return partition3_dp_inner(souvenirs, 1)


def partition3_recursion(souvenirs):
    value_total = sum(souvenirs)

    if value_total % 3 != 0:
        return 0

    value_per_partition_total = value_total // 3

    def optimal_weight_inner(weight_total_left, items, depth):
        for i in range(0, len(items)):
            item = items[i]
            # print('gold brick: {}'.format(gold_brick))

            if weight_total_left - item > 0 and len(items) > 1:
                value = optimal_weight_inner(weight_total_left - item, [items[j] for j in range(0, len(items)) if j != i], depth)
                if value == 1:
                    return 1
            elif weight_total_left - item == 0:
                if depth == 3:
                    return 1
                value = optimal_weight_inner(value_per_partition_total, [items[j] for j in range(0, len(items)) if j != i], depth+1)
                if value == 1:
                    return 1

        return 0

    return optimal_weight_inner(value_per_partition_total, souvenirs, 1)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
