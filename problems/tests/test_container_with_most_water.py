# coding: utf-8

import unittest

from problems.container_with_most_water import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            [1, 8, 6, 2, 5, 4, 8, 3, 7],
            [2, 3, 4, 5, 18, 17, 6],
            [1, 1],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        ]
        expected_output = [
            49,
            17,
            1,
            25,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.maxArea(data), output)


if __name__ == '__main__':
    unittest.main()
