# coding: utf-8

"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

from typing import List


class Solution1:
    def search(self, nums: List[int], target: int) -> int:

        # O(n)
        try:
            return nums.index(target)
        except ValueError:
            return -1


class Solution2:
    def search(self, nums: List[int], target: int) -> int:

        # O(logn)
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1
