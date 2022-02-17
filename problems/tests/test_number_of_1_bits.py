# coding: utf-8

import unittest

from problems.number_of_1_bits import Solution1, Solution2, Solution3


class TestCase(unittest.TestCase):
    def setUp(self):

        self.input_data = [
            int('00000000000000000000000000001011', base=2),
            int('00000000000000000000000010000000', base=2),
            int('11111111111111111111111111111101', base=2),
        ]
        self.expected_output = [
            3,
            1,
            31,
        ]

    def test_solution1(self):
        solution = Solution1()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.hammingWeight(data), output)

    def test_solution2(self):
        solution = Solution2()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.hammingWeight(data), output)

    def test_solution3(self):
        solution = Solution3()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.hammingWeight(data), output)


if __name__ == '__main__':
    unittest.main()
