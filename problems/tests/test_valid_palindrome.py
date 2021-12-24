# coding: utf-8

import unittest

from problems.valid_palindrome import Solution1, Solution2, Solution3


class TestCase(unittest.TestCase):
    def setUp(self):

        self.input_data = ['A man, a plan, a canal: Panama', 'race a car', ' ', 'ab_a', '0a', '.,']
        self.expected_output = [True, False, True, True, False, True]

    def test_solution1(self):
        solution = Solution1()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.isPalindrome(data), output)

    def test_solution2(self):
        solution = Solution2()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.isPalindrome(data), output)

    def test_solution3(self):
        solution = Solution3()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.isPalindrome(data), output)


if __name__ == '__main__':
    unittest.main()
