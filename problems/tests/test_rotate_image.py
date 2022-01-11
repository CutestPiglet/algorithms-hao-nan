# coding: utf-8

import unittest

from problems.rotate_image import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            [[10]],
        ]
        expected_output = [
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
            [[10]],
        ]
        for data, output in zip(input_data, expected_output):
            self.solution.rotate(data)
            self.assertEqual(data, output)


if __name__ == '__main__':
    unittest.main()
