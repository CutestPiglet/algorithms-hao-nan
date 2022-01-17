# coding: utf-8

"""
https://leetcode.com/problems/merge-intervals/
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])

        output = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= output[-1][-1]:
                output[-1][-1] = max(interval[-1], output[-1][-1])
            else:
                output.append(interval)

        return output
