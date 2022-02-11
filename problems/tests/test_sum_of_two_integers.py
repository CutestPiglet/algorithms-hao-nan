# coding: utf-8

import unittest

from problems.sum_of_two_integers import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            {'a': 1, 'b': 2},
            {'a': -1000, 'b': 1000},
        ]
        expected_output = [
            3,
            0,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.getSum(data['a'], data['b']), output)


if __name__ == '__main__':
    unittest.main()
