# coding: utf-8

"""
https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {
            # num: index
        }
        for index, num in enumerate(nums):
            if num in diff:
                return [diff[num], index]

            diff[target - num] = index
