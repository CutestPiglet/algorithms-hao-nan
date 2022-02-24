# coding: utf-8

"""
https://leetcode.com/problems/invert-binary-tree/
"""

from typing import Optional

from problems.utils import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root:
            root.left, root.right = root.right, root.left

            self.invertTree(root.left)
            self.invertTree(root.right)

            return root
