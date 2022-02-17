# coding: utf-8

import unittest

from problems.decode_ways import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            '12',
            '226',
            '06',
        ]
        expected_output = [
            2,
            3,
            0,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.numDecodings(data), output)


if __name__ == '__main__':
    unittest.main()
