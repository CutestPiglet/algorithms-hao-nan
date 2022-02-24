# coding: utf-8

from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_list_to_listnode(values, pos=-1):
    """
    Convert list to ListNode

    Args:
        values (list): list of ListNode values
        pos (int): denote the index of the node that tail's next pointer is connected to

    Returns:
        ListNode: head pointer of ListNodes
    """

    dummy_head_node = ListNode()
    current_node = dummy_head_node

    cycle_node = None
    for index, value in enumerate(values):
        current_node.next = ListNode(value)
        current_node = current_node.next

        if index == pos:
            cycle_node = current_node

    if cycle_node:
        current_node.next = cycle_node

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
        if values[i].strip() == 'null':
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

        try:
            right_value = value_queue.popleft()
        except IndexError:
            continue

        if right_value is not None:
            node.right = TreeNode(right_value)
            node_queue.append(node.right)

    return root


def serialize_treenode(root):
    """
    Deserialize string format of TreeNodes to binary TreeNodes

    Args:
        TreeNode (root): root TreeNode

    Returns:
        str: string format of TreeNodes
    """

    if not root:
        return '[]'

    values = []
    node_queue = deque([root])

    while node_queue:
        node = node_queue.popleft()
        if node:
            values.append(node.val)
            node_queue.append(node.left)
            node_queue.append(node.right)
        else:
            values.append('null')

    while values and (values[-1] == 'null'):
        values.pop()

    return f"[{', '.join(str(i) for i in values)}]"
