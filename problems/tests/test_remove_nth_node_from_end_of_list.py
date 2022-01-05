# coding: utf-8

import unittest

from problems.remove_nth_node_from_end_of_list import Solution1, Solution2
from problems.utils import convert_list_to_listnode, convert_listnode_to_list


class TestCase(unittest.TestCase):
    def setUp(self):

        self.input_data = [
            {'head': [1, 2, 3, 4, 5], 'n': 2},
            {'head': [1], 'n': 1},
            {'head': [1, 2], 'n': 1},
        ]
        self.expected_output = [
            [1, 2, 3, 5],
            [],
            [1],
        ]

    def test_solution1(self):
        solution = Solution1()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(
                convert_listnode_to_list(solution.removeNthFromEnd(convert_list_to_listnode(data['head']), data['n'])),
                output,
            )

    def test_solution2(self):
        solution = Solution2()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(
                convert_listnode_to_list(solution.removeNthFromEnd(convert_list_to_listnode(data['head']), data['n'])),
                output,
            )


if __name__ == '__main__':
    unittest.main()
