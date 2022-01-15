from majority_element import get_majority_element
import unittest
import random

class TestBinarySearch(unittest.TestCase):

    def test_get_majority_element(self):
        for _ in range(500):
            self.assertEqual(1, get_majority_element([2, 1, 1], 0, 3))
            self.assertEqual(1, get_majority_element([1, 1, 2], 0, 3))
            self.assertEqual(-1, get_majority_element([1, 3, 2], 0, 3))
            self.assertEqual(1, get_majority_element([2, 3, 9, 2, 2], 0, 5))

    def test_get_majority_element_stress_positive(self):
        for i in range(10):
            a = []
            for _ in range(100):
                a.append(500)

            for _ in range(99):
                a.append(random.randint(0, 500))

            random.shuffle(a)
            result = get_majority_element(a, 0, len(a))

            if result != 1:
                print("Size: " + str(len(a)))
                print(a)
            else:
                print("Success: {}".format(i))

            self.assertEqual(1, result)

    def test_get_majority_element_stress_negative(self):
        for i in range(10):
            a = []
            for _ in range(100):
                a.append(500)

            for _ in range(100):
                a.append(random.randint(0, 499))

            random.shuffle(a)
            result = get_majority_element(a, 0, len(a))

            if result != -1:
                print("Size: " + str(len(a)))
                print(a)
            else:
                print("Success: {}".format(i))

            self.assertEqual(-1, result)
