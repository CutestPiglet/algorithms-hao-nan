# coding: utf-8

import unittest

from problems.two_sum import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            {'nums': [2, 7, 11, 15], 'target': 18},
            {'nums': [3, 2, 4], 'target': 7},
            {'nums': [3, 3], 'target': 6},
            {'nums': [2, 4, 7, 11, 15, 3], 'target': 5},
        ]
        expected_output = [
            [1, 2],
            [0, 2],
            [0, 1],
            [0, 5],
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.twoSum(data['nums'], data['target']), output)


if __name__ == '__main__':
    unittest.main()
