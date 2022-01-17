# coding: utf-8

import unittest

from problems.merge_intervals import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 4], [4, 5]],
            [[1, 4], [0, 4]],
            [[1, 4], [0, 1]],
            [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]],
        ]
        expected_output = [
            [[1, 6], [8, 10], [15, 18]],
            [[1, 5]],
            [[0, 4]],
            [[0, 4]],
            [[1, 10]],
        ]
        for data, output in zip(input_data, expected_output):
            self.assertListEqual(self.solution.merge(data), output)


if __name__ == '__main__':
    unittest.main()
