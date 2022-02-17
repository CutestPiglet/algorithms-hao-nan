# coding: utf-8

"""
https://leetcode.com/problems/number-of-1-bits/
"""


class Solution1:
    def hammingWeight(self, n: int) -> int:

        return len(list(filter(lambda x: x == '1', f'{n:b}')))


class Solution2:
    def hammingWeight(self, n: int) -> int:

        return bin(n).count('1')


class Solution3:
    def hammingWeight(self, n: int) -> int:

        output = 0

        for i in range(32):
            output += (n & 1)
            n = n >> 1

        return output
