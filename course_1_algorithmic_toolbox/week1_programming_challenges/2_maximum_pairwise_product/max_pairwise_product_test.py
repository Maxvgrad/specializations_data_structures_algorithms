from max_pairwise_product import max_pairwise_product, max_pairwise_product_naive
import unittest
import random


class TestMaxPairwiseProduct(unittest.TestCase):

    def test_max_pairwise(self):
        self.assertEqual(60, max_pairwise_product([3, 5, 6, 10]))
        self.assertEqual(60, max_pairwise_product_naive([3, 5, 6, 10]))

    def test_max_pairwise_2(self):
        self.assertEqual(6, max_pairwise_product([1, 2, 3]))

    def test_max_pairwise_3(self):
        self.assertEqual(2, max_pairwise_product([1, 2]))
        self.assertEqual(2, max_pairwise_product([2, 1]))
        self.assertEqual(7680243769, max_pairwise_product([68165, 87637, 74297, 2904, 32873, 86010, 87637, 66131, 82858, 82935]))

    # StressTest(N,M): while true:
    # n ← random integer between 2 and N allocate array A[1...n]
    # fori from1ton:
    # A[i] ← random integer between 0 and M print(A[1 . . . n])
    # result1 ← MaxPairwiseProductNaive(A) result2 ← MaxPairwiseProductFast(A)
    # if result1 = result2: print(“OK”)
    # else:
    # print(“Wrong answer: ”, result1, result2) return

    def test_stress_max_pairwise_product(self):
        counter = 0
        arr_max_len = 5
        max_number_in_arr = 9
        while counter < 50:
            numbers = []
            n = random.randint(2, arr_max_len)
            for i in range(n):
                numbers.append(random.randint(0, max_number_in_arr))

            product_naive = max_pairwise_product_naive(numbers)
            product_fast = max_pairwise_product(numbers)

            if product_naive != product_fast:
                print('Wrong result')
                print(numbers)
                self.assertEqual(product_naive, product_fast)

            counter = counter + 1
