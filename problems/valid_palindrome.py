# coding: utf-8

"""
https://leetcode.com/problems/valid-palindrome/
"""


class Solution1:
    def isPalindrome(self, s: str) -> bool:

        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char.lower())

        if len(chars) < 2:
            return True

        left, right = 0, len(chars) - 1

        while left <= right:
            if chars[left] != chars[right]:
                return False

            left += 1
            right -= 1

        return True


class Solution2:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False

                left += 1
                right -= 1

        return True


class Solution3:
    def isPalindrome(self, s: str) -> bool:

        import re

        s = re.sub('[^a-z0-9]', '', s.lower())

        return s == ''.join(reversed(s))
