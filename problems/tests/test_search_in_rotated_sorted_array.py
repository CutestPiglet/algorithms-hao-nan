# coding: utf-8

import unittest

from problems.search_in_rotated_sorted_array import Solution1, Solution2


class TestCase(unittest.TestCase):
    def setUp(self):

        self.input_data = [
            {'nums': [4, 5, 6, 7, 0, 1, 2], 'target': 0},
            {'nums': [4, 5, 6, 7, 0, 1, 2], 'target': 3},
            {'nums': [1], 'target': 0},
            {'nums': [3, 1], 'target': 1},
        ]
        self.expected_output = [
            4,
            -1,
            -1,
            1,
        ]

    def test_solution1(self):
        solution = Solution1()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.search(data['nums'], data['target']), output)

    def test_solution2(self):
        solution = Solution2()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.search(data['nums'], data['target']), output)


if __name__ == '__main__':
    unittest.main()
