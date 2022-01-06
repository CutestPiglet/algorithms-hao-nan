# coding: utf-8

import unittest

from problems.valid_parentheses import Solution


class TestCase(unittest.TestCase):
    def setUp(self):

        self.input_data = [
            '()',
            '()[]{}',
            '(]',
            '([)]',
            '[',
            ']',
        ]
        self.expected_output = [
            True,
            True,
            False,
            False,
            False,
            False,
        ]

    def test(self):
        solution = Solution()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.isValid(data), output)


if __name__ == '__main__':
    unittest.main()
