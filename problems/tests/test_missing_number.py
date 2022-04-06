# coding: utf-8

import unittest

from problems.missing_number import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            [3, 0, 1],
            [0, 1],
            [9, 6, 4, 2, 3, 5, 7, 0, 1],
        ]
        expected_output = [
            2,
            2,
            8,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.missingNumber(data), output)


if __name__ == '__main__':
    unittest.main()
