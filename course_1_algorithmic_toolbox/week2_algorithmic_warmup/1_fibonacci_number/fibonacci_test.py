from fibonacci import calc_fib_naive, calc_fib
import unittest


class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(13, calc_fib_naive(7))
        self.assertEqual(13, calc_fib(7))
