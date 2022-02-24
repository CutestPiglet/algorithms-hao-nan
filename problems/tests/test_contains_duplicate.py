# coding: utf-8

import unittest

from problems.contains_duplicate import Solution1, Solution2


class TestCase(unittest.TestCase):
    def setUp(self):

        self.input_data = [
            [1, 2, 3, 1],
            [1, 2, 3, 4],
            [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
        ]
        self.expected_output = [
            True,
            False,
            True,
        ]

    def test_solution1(self):
        solution = Solution1()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.containsDuplicate(data), output)

    def test_solution2(self):
        solution = Solution2()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.containsDuplicate(data), output)


if __name__ == '__main__':
    unittest.main()
