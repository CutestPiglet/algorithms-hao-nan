# coding: utf-8

"""
https://leetcode.com/problems/sum-of-two-integers/
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xfff

        while (b & mask) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        # avoid overflow
        return (a & mask) if b > 0 else a
