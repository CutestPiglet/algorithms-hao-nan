# coding: utf-8

"""
https://leetcode.com/problems/linked-list-cycle/
"""

from typing import Optional

from problems.utils import ListNode


class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = set()

        while head:
            if head not in seen:
                seen.add(head)
                head = head.next
            else:
                return True

        return False


class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
