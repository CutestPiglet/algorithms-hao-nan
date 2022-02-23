# coding: utf-8

"""
https://leetcode.com/problems/reverse-bits/
"""


class Solution:
    def reverseBits(self, n: int) -> int:

        return int(bin(n)[2:].rjust(32, '0')[::-1], 2)
