# coding: utf-8

import unittest

from problems.spiral_matrix import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [[2], [3]],
            [[7], [6], [9]],
            [[100]],
        ]
        expected_output = [
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            [2, 3],
            [7, 6, 9],
            [100],
        ]
        for data, output in zip(input_data, expected_output):
            self.assertListEqual(self.solution.spiralOrder(data), output)


if __name__ == '__main__':
    unittest.main()
