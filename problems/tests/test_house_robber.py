# coding: utf-8

import unittest

from problems.house_robber import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            [1, 2, 3, 1],
            [2, 7, 9, 3, 1],
        ]
        expected_output = [
            4,
            12,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.rob(data), output)


if __name__ == '__main__':
    unittest.main()
