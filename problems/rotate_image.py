# coding: utf-8

"""
https://leetcode.com/problems/rotate-image/
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)

        # reverse
        i, j = 0, m - 1
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1

        # transpose
        for i in range(m):
            for j in range(i, m):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
