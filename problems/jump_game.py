# coding: utf-8

"""
https://leetcode.com/problems/jump-game/
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        target_index = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target_index:
                target_index = i

        return not target_index
