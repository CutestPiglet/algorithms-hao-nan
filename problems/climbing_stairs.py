# coding: utf-8

"""
https://leetcode.com/problems/climbing-stairs/
"""


class Solution1:
    def climbStairs(self, n: int) -> int:

        ways = [1, 2]

        for i in range(2, n):
            ways.append(ways[i - 1] + ways[i - 2])

        return ways[n - 1]


class Solution2:
    def climbStairs(self, n: int) -> int:
        output = prev = 1

        for _ in range(n - 1):
            output, prev = output + prev, output

        return output
