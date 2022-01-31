# Uses python3
import sys

def get_change_recursive(m, coins=[1, 3, 4]):

    if coins is None:
        coins = [1, 3, 4]

    def get_change_inner(money):
        if money == 0:
            return 0

        min_num_of_coins = -1

        for coin in coins:
            if money >= coin:
                number_of_coins = get_change_inner(money-coin)

                if min_num_of_coins == -1 or (number_of_coins + 1) < min_num_of_coins:
                    min_num_of_coins = number_of_coins + 1

        return min_num_of_coins

    #write your code here
    return get_change_inner(m)

def get_change(m, coins=[1, 3, 4]):
    change_dic = {0: 0}
    for money in range(1, m+1):
        change_dic[money] = -1
        for coin in coins:
            if coin <= money:
                number_of_change = change_dic[money-coin] + 1
                if change_dic[money] == -1 or number_of_change < change_dic[money]:
                    change_dic[money] = number_of_change

    return change_dic[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
