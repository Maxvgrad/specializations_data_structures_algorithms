# Uses python3
def calc_fib_naive(n):
    if n <= 1:
        return n

    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)

def calc_fib(n):
    if (n <= 1):
        return n
    f_n_minus_one = 1
    f_n_minus_two = 0

    for i in range(2, n):
        tmp = f_n_minus_one
        f_n_minus_one = f_n_minus_one + f_n_minus_two
        f_n_minus_two = tmp

    return f_n_minus_one + f_n_minus_two

n = int(input())
print(calc_fib(n))
