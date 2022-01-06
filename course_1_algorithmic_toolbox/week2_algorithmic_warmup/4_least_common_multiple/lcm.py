# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def lcm(a, b):
    step = max(a, b)
    result = step
    divider = min(a, b)
    for _ in range(divider):
        if result % divider == 0:
            return result
        result = result + step
    return result # not possible

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

