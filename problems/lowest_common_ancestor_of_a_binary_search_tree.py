# coding: utf-8

"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""

from typing import Optional

from problems.utils import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:

        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
