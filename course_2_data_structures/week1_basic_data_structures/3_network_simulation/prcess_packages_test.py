from process_packages import process_requests, Request, Buffer, Response
import unittest
import random


class TestProcessPackages(unittest.TestCase):

    def test_process_packages(self):
        for i in range(1, 23):
            file_path = get_file_path(i)
            print(file_path)
            requests = []
            buffer = None
            n_requests = 0
            with open(file_path, 'r') as file:
                buffer_size, n_requests = map(int, file.readline().split())
                buffer = Buffer(buffer_size)
                for _ in range(n_requests):
                    arrived_at, time_to_process = map(int, file.readline().split())
                    requests.append(Request(arrived_at, time_to_process))

            responses_answer = []
            with open(get_file_path_answer(file_path), 'r') as file_answer:
                for _ in range(n_requests):
                    started_at = int(file_answer.readline())
                    response = Response(started_at == -1, started_at)
                    responses_answer.append(response)

            responses = process_requests(requests, buffer)

            for i in range(0, len(responses)):
                self.assertEqual(responses_answer[i], responses[i], file_path)

        self.assertTrue(True)


def get_file_path(i):
    file_name = str(i)
    if len(file_name) == 1:
        file_name = '0' + file_name
    return './tests/{}'.format(file_name)


def get_file_path_answer(file_path):
    return file_path + '.a'
