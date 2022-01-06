from fibonacci_last_digit import get_fibonacci_last_digit, get_fibonacci_last_digit_naive
import unittest


class TestFibonacciLastDigit(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(3, get_fibonacci_last_digit_naive(7))
        self.assertEqual(3, get_fibonacci_last_digit(7))
