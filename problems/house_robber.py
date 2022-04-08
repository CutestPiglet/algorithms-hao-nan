# coding: utf-8

"""
https://leetcode.com/problems/house-robber/
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        rob, not_rob = 0, 0

        for num in nums:
            # explain var name of this line: rob curr house, not rob curr house = not rob prev house + num, max(rob prev house, not rob prev house)
            rob, not_rob = not_rob + num, max(rob, not_rob)

        return max(rob, not_rob)
