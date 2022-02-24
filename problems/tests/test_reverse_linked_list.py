# coding: utf-8

import unittest

from problems.reverse_linked_list import Solution
from problems.utils import convert_list_to_listnode, convert_listnode_to_list


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            [1, 2, 3, 4, 5],
            [1, 2],
            [7],
            [],
        ]
        expected_output = [
            [5, 4, 3, 2, 1],
            [2, 1],
            [7],
            [],
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(
                convert_listnode_to_list(self.solution.reverseList(convert_list_to_listnode(data))),
                output,
            )


if __name__ == '__main__':
    unittest.main()
