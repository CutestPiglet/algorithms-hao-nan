# coding: utf-8

import unittest

from problems.number_of_islands import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']],
            [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']],
        ]
        expected_output = [
            1,
            3,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.numIslands(data), output)


if __name__ == '__main__':
    unittest.main()
