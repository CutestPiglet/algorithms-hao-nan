# coding: utf-8

import unittest

from problems.climbing_stairs import Solution1, Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.input_data = [
            2,
            3,
            7,
        ]
        self.expected_output = [
            2,
            3,
            21,
        ]

    def test_solution1(self):
        solution = Solution1()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.climbStairs(data), output)

    def test_solution2(self):
        solution = Solution2()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.climbStairs(data), output)


if __name__ == '__main__':
    unittest.main()
