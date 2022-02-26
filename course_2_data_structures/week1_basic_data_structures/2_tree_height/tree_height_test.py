from tree_height import compute_height
import unittest
import random


class TestComputeHeight(unittest.TestCase):

    def test_when_match_should_return_success(self):
        for i in range(1, 25):
            file_path = get_file_path(i)
            n = None
            p = None
            answer = None
            with open(get_file_path(i), 'r') as file:
                n = int(file.readline())
                p = list(map(int, file.readline().split()))
            with open(get_file_path_answer(file_path), 'r') as file_answer:
                answer = int(file_answer.readline())
            print('Test case: ' + file_path)
            self.assertEqual(answer, compute_height(n, p), file_path)

        self.assertTrue(True)


def get_file_path(i):
    file_name = str(i)
    if len(file_name) == 1:
        file_name = '0' + file_name
    return './tests/{}'.format(file_name)


def get_file_path_answer(file_path):
    return file_path + '.a'
