# coding: utf-8

"""
https://leetcode.com/problems/missing-number/
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        return sum(range(len(nums) + 1)) - sum(nums)
