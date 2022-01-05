# coding: utf-8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_list_to_listnode(values):
    """
    Convert list to ListNode

    Args:
        values (list): list of ListNode values

    Returns:
        ListNode: head pointer of ListNodes
    """

    dummy_head_node = ListNode()
    current_node = dummy_head_node

    for value in values:
        current_node.next = ListNode(value)
        current_node = current_node.next

    return dummy_head_node.next


def convert_listnode_to_list(head):
    """
    Convert ListNode to list of values

    Args:
        head (ListNode): head pointer of ListNodes

    Returns:
        list: list of ListNode values
    """

    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values
