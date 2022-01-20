# coding: utf-8

import unittest

from problems.set_matrix_zeroes import Solution1, Solution2


class TestCase(unittest.TestCase):
    def setUp(self):

        self.input_data = [
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
        ]
        self.expected_output = [
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ]

    def test_solution1(self):
        solution = Solution1()
        for data, output in zip(self.input_data, self.expected_output):
            solution.setZeroes(data)
            self.assertEqual(data, output)

    def test_solution2(self):
        solution = Solution2()
        for data, output in zip(self.input_data, self.expected_output):
            solution.setZeroes(data)
            self.assertEqual(data, output)


if __name__ == '__main__':
    unittest.main()
