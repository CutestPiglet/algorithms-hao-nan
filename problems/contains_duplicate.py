# coding: utf-8

"""
https://leetcode.com/problems/contains-duplicate/
"""

from typing import List


class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:

        return len(nums) != len(set(nums))


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True

        return False
