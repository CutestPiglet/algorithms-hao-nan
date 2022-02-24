# coding: utf-8

import unittest

from problems.invert_binary_tree import Solution
from problems.utils import deserialize_tree_str, serialize_treenode


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            '[4, 2, 7, 1, 3, 6, 9]',
            '[2, 1, 3]',
            '[1, null, 3]',
            '[1, 2]',
            '[7]',
            '[]',
        ]
        expected_output = [
            '[4, 7, 2, 9, 6, 3, 1]',
            '[2, 3, 1]',
            '[1, 3]',
            '[1, null, 2]',
            '[7]',
            '[]',
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(
                serialize_treenode(self.solution.invertTree(deserialize_tree_str(data))),
                output,
            )


if __name__ == '__main__':
    unittest.main()
