# coding: utf-8

"""
https://leetcode.com/problems/decode-ways/
"""


class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0

        ways = [1] * len(s)

        for i in range(1, len(s)):
            ways[i] = 0 if s[i] == '0' else ways[i - 1]

            if 10 <= int(s[i - 1:i + 1]) <= 26:
                ways[i] += ways[i - 2 if i > 1 else 0]

        return ways[-1]
