# coding: utf-8

"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

from typing import Optional

from problems.utils import ListNode


class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        pointer, len_of_head = head, 0
        while pointer:
            pointer = pointer.next
            len_of_head += 1

        if len_of_head == n:
            return head.next

        pointer = head
        for i in range(1, len_of_head - n):
            pointer = pointer.next

        pointer.next = pointer.next.next

        return head


class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        current_node = previous_of_nth_node = head

        # iterate n nodes
        for _ in range(n):
            current_node = current_node.next

        # n is len of ListNodes
        if not current_node:
            return head.next

        # keep n nodes gap between previous_of_nth_node and current_node
        while current_node.next:
            current_node = current_node.next
            previous_of_nth_node = previous_of_nth_node.next

        # since previous_of_nth_node is (n + 1)th node from end, just remove the nth node
        previous_of_nth_node.next = previous_of_nth_node.next.next

        return head
