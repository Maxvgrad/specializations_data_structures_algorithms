from sorting import randomized_quick_sort, partition3
import unittest
import random


class TestImprovingQuickSort(unittest.TestCase):

    def test_randomized_quick_sort(self):
        a = [1, 33, 5, 8, 12, 13]
        randomized_quick_sort(a, 0, len(a) - 1)
        self.assertEqual([1, 5, 8, 12, 13, 33], a, partition3)

    def test_randomized_quick_sort_2(self):
        a = []
        for i in range(1, 5):
            k = random.randint(0, 100)
            for _ in range(i):
                a.append(k)
        random.shuffle(a)

        a2 = a.copy()
        randomized_quick_sort(a, 0, len(a) - 1, partition3)
        a2.sort()
        self.assertEqual(a2, a)

    def test_partition_3_swap(self):
        x = 10
        a = [1, 3, 5, 10, 10, 10, 33, 7, 10, 12, 13]
        i = 6

        j = 5
        k = 2
        self.assertEqual(5, a[k])
        self.assertEqual(10, a[k+1])
        self.assertEqual(10, a[j])
        self.assertEqual(33, a[j+1])

        i += 1
        self.assertEqual(7, a[i])
        self.assertTrue(a[i] < x)

        j += 1
        k += 1

        a[j], a[i] = a[i], a[j]
        a[k], a[j] = a[j], a[k]

        self.assertEqual([1, 3, 5, 7, 10, 10, 10, 33, 10, 12, 13], a)

        i += 1
        self.assertTrue(a[i] == x)
        j += 1

        a[j], a[i] = a[i], a[j]

        self.assertEqual([1, 3, 5, 7, 10, 10, 10, 10, 33, 12, 13], a)




