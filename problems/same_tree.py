# coding: utf-8

"""
https://leetcode.com/problems/same-tree/
"""

from typing import Optional

from problems.utils import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)

        return p == q
