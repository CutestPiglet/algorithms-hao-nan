# coding: utf-8

"""
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        close_brackets = ['dummy']

        for bracket_char in s:
            if bracket_char in brackets:
                close_brackets.append(brackets[bracket_char])
            elif bracket_char != close_brackets.pop():
                return False

        return not len(close_brackets) > 1
