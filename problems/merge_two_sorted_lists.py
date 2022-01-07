# coding: utf-8

"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""

from typing import Optional

from problems.utils import ListNode


class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = current = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2

        return dummy.next


class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1 or list2
