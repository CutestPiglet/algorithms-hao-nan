# coding: utf-8

"""
https://leetcode.com/problems/maximum-subarray/
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        output = candidate = nums[0]

        for num in nums[1:]:
            candidate = max(num, num + candidate)
            output = max(output, candidate)

        return output
