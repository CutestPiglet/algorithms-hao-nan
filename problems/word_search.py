# coding: utf-8

"""
https://leetcode.com/problems/word-search/
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if self.search_word(board, i, j, m, n, word):
                    return True

        return False

    def search_word(self, board, i, j, m, n, word):

        # all chars are found
        if not word:
            return True

        if i < 0 or i == m or j < 0 or j == n or word[0] != board[i][j]:
            return False

        # found a single char (word[0])

        board[i][j] = '&'  # avoid traverse again

        # check remaining chars
        target_word = word[1:]
        result = self.search_word(board, i - 1, j, m, n, target_word) or \
            self.search_word(board, i + 1, j, m, n, target_word) or \
            self.search_word(board, i, j + 1, m, n, target_word) or \
            self.search_word(board, i, j - 1, m, n, target_word)

        board[i][j] = word[0]  # set to original value

        return result
