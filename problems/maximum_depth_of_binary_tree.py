# coding: utf-8

"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

from typing import Optional

from problems.utils import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
