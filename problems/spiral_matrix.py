# coding: utf-8

"""
https://leetcode.com/problems/spiral-matrix/
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        output = []

        while matrix:
            output.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]

        return output
