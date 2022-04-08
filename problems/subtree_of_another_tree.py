# coding: utf-8

"""
https://leetcode.com/problems/subtree-of-another-tree/
"""

from typing import Optional

from problems.utils import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return self.check_subtree(root, subRoot)

    def check_subtree(self, root_node, sub_root):
        if not root_node:
            return False

        if self.is_same_tree(root_node, sub_root):
            return True

        return self.check_subtree(root_node.left, sub_root) or self.check_subtree(root_node.right, sub_root)

    def is_same_tree(self, p, q):

        if p and q and p.val == q.val:
            return self.is_same_tree(p.left, q.left) & self.is_same_tree(p.right, q.right)

        return p == q
