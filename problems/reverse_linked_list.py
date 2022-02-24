# coding: utf-8

"""
https://leetcode.com/problems/reverse-linked-list/
"""

from typing import Optional

from problems.utils import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        prev, tail = None, head
        while tail:
            tmp = tail.next
            tail.next = prev
            prev = tail
            tail = tmp

        return prev
