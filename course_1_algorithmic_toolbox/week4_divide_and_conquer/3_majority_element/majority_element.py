# Uses python3
import sys
import random
import math


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    half = right//2
    major = half+1

    def randomized_quick_sort(a, l, r):
        # print("l={}, r={}".format(l,r))
        if r < l or r - l + 1 < major:
            return -1

        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        # use partition3
        left_boundary, right_boundary = partition3(a, l, r)

        if right_boundary - left_boundary + 1 >= major:
            return 1

        if (left_boundary-l) > (r - right_boundary):
            return randomized_quick_sort(a, l, left_boundary - 1)
        else:
            return randomized_quick_sort(a, right_boundary + 1, r)

    return randomized_quick_sort(a, left, right-1)


def partition3(a, l, r):
    x = a[l]
    j = l  # max boundary index of x area
    k = l  # boundary index below x
    # print("x={}".format(x))
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[j], a[i] = a[i], a[j]
            if a[k] < x:
                k += 1
                a[k], a[j] = a[j], a[k]
            else:
                a[k], a[j] = a[j], a[k]

        elif a[i] == x:
            j += 1
            a[j], a[i] = a[i], a[j]

    # a[l], a[j] = a[j], a[l]
    if a[k] == x:
        return k, j

    return k+1, j

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
