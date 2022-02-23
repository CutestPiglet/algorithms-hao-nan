# coding: utf-8

import unittest

from problems.reverse_bits import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            43261596,
            4294967293,
        ]
        expected_output = [
            964176192,
            3221225471,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.reverseBits(data), output)


if __name__ == '__main__':
    unittest.main()
