# Uses python3
import sys


def get_change(m):
    result = 0
    coins = [10, 5, 1]
    amount_to_change = m
    for coin in coins:
        result = result + amount_to_change // coin
        amount_to_change = amount_to_change % coin
    return result


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
