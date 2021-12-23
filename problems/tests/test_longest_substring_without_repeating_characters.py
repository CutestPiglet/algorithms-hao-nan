# coding: utf-8

import unittest

from problems.longest_substring_without_repeating_characters import (Solution1,
                                                                     Solution2)


class TestCase(unittest.TestCase):
    def setUp(self):

        self.input_data = ['abcabcbb', 'bbbbb', 'pwwkew', ' ', '', 'aab', 'acbdbacd']
        self.expected_output = [3, 1, 3, 1, 0, 2, 4]

    def test_solution1(self):
        solution = Solution1()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.lengthOfLongestSubstring(data), output)

    def test_solution2(self):
        solution = Solution2()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.lengthOfLongestSubstring(data), output)


if __name__ == '__main__':
    unittest.main()
