# coding: utf-8

"""
https://leetcode.com/problems/set-matrix-zeroes/
"""

from typing import List


class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for up_i in range(i):
                        matrix[up_i][j] = 0
                    for left_j in range(j):
                        matrix[i][left_j] = 0
                    for right_j in range(j + 1, n):
                        if matrix[i][right_j] != 0:
                            matrix[i][right_j] = 'X'
                    for down_i in range(i + 1, m):
                        if matrix[down_i][j] != 0:
                            matrix[down_i][j] = 'X'

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'X':
                    matrix[i][j] = 0


class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        first_row_has_zero, first_col_has_zero = False, False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_has_zero = True
                    if j == 0:
                        first_col_has_zero = True
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = 0 if matrix[0][j] == 0 or matrix[i][0] == 0 else matrix[i][j]

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
