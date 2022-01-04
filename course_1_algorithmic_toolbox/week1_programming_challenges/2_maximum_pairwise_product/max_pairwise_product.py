
def max_pairwise_product_naive(numbers):
    n = len(numbers)
    product = 0
    for i in range(n):
        for j in range(i + 1, n):
            product = max(product, numbers[i] * numbers[j])
    return product


def max_pairwise_product(numbers):
    n = len(numbers)

    if n == 3:
        max_a = numbers[0]
        max_i = 0

        for i in range(1, 3):
            if max_a < numbers[i]:
                max_a = numbers[i]
                max_i = i

        max_j = 0
        if max_i == 0:
            max_j = 1

        for j in range(3):
            if j != max_i and numbers[max_j] < numbers[j]:
                max_j = j

        return max_a * numbers[max_j]

    max_a = max(numbers[0], numbers[1])
    max_b = min(numbers[0], numbers[1])

    for i in range(2, n):
        a = numbers[i]
        if max_a < a:
            max_b = max_a
            max_a = a
        elif max_b < a:
            max_b = a

    return max_b * max_a


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
