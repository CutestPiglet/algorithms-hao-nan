# coding: utf-8

import unittest

from problems.counting_bits import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            2,
            5,
        ]
        expected_output = [
            [0, 1, 1],
            [0, 1, 1, 2, 1, 2],
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.countBits(data), output)


if __name__ == '__main__':
    unittest.main()
