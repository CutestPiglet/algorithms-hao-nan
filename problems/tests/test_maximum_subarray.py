# coding: utf-8

import unittest

from problems.maximum_subarray import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            [2],
            [5, 4, -1, 7, 8],
        ]
        expected_output = [
            6,
            2,
            23,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.maxSubArray(data), output)


if __name__ == '__main__':
    unittest.main()
