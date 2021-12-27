# coding: utf-8

"""
https://leetcode.com/problems/container-with-most-water/
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        max_area = 0

        while left <= right:
            w = right - left
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1

            max_area = max(max_area, h * w)  # height * width

        return max_area
