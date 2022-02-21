# coding: utf-8

from collections import deque


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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize_tree_str(s):
    """
    Deserialize string format of TreeNodes to binary TreeNodes

    Args:
        s (str): string format of TreeNodes

    Returns:
        TreeNode: root TreeNode
    """

    if s == '[]':
        return None

    values = s.strip('[]').split(',')
    for i in range(len(values)):
        if values[i] == 'null':
            values[i] = None
        else:
            values[i] = int(values[i])

    value_queue = deque(values)

    root = TreeNode(value_queue.popleft())
    node_queue = deque([root])

    while node_queue and value_queue:
        node = node_queue.popleft()

        left_value = value_queue.popleft()
        if left_value is not None:
            node.left = TreeNode(left_value)
            node_queue.append(node.left)

        right_value = value_queue.popleft()
        if right_value is not None:
            node.right = TreeNode(right_value)
            node_queue.append(node.right)

    return root
