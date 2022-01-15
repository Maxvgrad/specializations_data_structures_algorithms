# Uses python3
import sys
import random


def partition3(a, l, r):
    x = a[l]
    j = l  # max boundary index of x area
    k = l  # boundary index below x
    # print("x={}".format(x))
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[j], a[i] = a[i], a[j]
            if j-k > 1:
                k += 1
                a[k], a[j] = a[j], a[k]
            else:
                a[k], a[j] = a[j], a[k]

        elif a[i] == x:
            j += 1
            a[j], a[i] = a[i], a[j]

    # a[l], a[j] = a[j], a[l]
    return k+1, j


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j, j


def randomized_quick_sort(a, l, r, partition=partition2):
    # print("l={}, r={}".format(l,r))
    if l >= r:
        return

    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    left_boundary, right_boundary = partition(a, l, r)
    # print(a)
    randomized_quick_sort(a, l, left_boundary - 1, partition)
    randomized_quick_sort(a, right_boundary + 1, r, partition)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1, partition3)
    for x in a:
        print(x, end=' ')
