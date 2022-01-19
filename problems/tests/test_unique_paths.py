# coding: utf-8

import unittest

from problems.unique_paths import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            {'m': 3, 'n': 7},
            {'m': 3, 'n': 2},
        ]
        expected_output = [
            28,
            3,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.uniquePaths(data['m'], data['n']), output)


if __name__ == '__main__':
    unittest.main()
