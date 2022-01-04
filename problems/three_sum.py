# coding: utf-8

"""
https://leetcode.com/problems/3sum/
"""

from typing import List


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        output = set()

        for index, num in enumerate(nums):
            self.two_sum(nums[index + 1:], -num, output)

        return output

    def two_sum(self, nums, target, output):

        seen = set()

        for index, num in enumerate(nums):
            if target - num in seen:
                output.add(tuple(sorted([-target, num, target - num])))

            seen.add(num)


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        from itertools import combinations

        output = set()

        neg_nums, pos_nums, zeros = [], [], []
        for num in nums:
            if num > 0:
                pos_nums.append(num)
            elif num < 0:
                neg_nums.append(num)
            else:
                zeros.append(num)

        neg_dict, pos_dict = dict.fromkeys(neg_nums), dict.fromkeys(pos_nums)

        if zeros:
            for num in pos_dict:
                if -num in neg_dict:
                    output.add((-num, 0, num))

        if len(zeros) >= 3:
            output.add((0, 0, 0))

        for x, y in combinations(neg_nums, 2):
            target = -(x + y)
            if target in pos_dict:
                output.add(tuple(sorted([x, y, target])))

        for x, y in combinations(pos_nums, 2):
            target = -(x + y)
            if target in neg_dict:
                output.add(tuple(sorted([x, y, target])))

        return output
