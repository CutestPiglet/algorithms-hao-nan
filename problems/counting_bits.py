# coding: utf-8

"""
https://leetcode.com/problems/counting-bits/
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = []
        for i in range(n + 1):
            ans.append(f'{i:b}'.count('1'))

        return ans
