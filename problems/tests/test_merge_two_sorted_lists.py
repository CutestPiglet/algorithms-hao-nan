# coding: utf-8

import unittest

from problems.merge_two_sorted_lists import Solution1, Solution2
from problems.utils import convert_list_to_listnode, convert_listnode_to_list


class TestCase(unittest.TestCase):
    def setUp(self):

        self.input_data = [
            {'list1': [1, 2, 4], 'list2': [1, 3, 4]},
            {'list1': [], 'list2': []},
            {'list1': [], 'list2': [0]},
            {'list1': [1, 2], 'list2': [3, 4]},
        ]
        self.expected_output = [
            [1, 1, 2, 3, 4, 4],
            [],
            [0],
            [1, 2, 3, 4],
        ]

    def test_solution1(self):
        solution = Solution1()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(
                convert_listnode_to_list(solution.mergeTwoLists(convert_list_to_listnode(data['list1']), convert_list_to_listnode(data['list2']))),
                output,
            )

    def test_solution2(self):
        solution = Solution2()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(
                convert_listnode_to_list(solution.mergeTwoLists(convert_list_to_listnode(data['list1']), convert_list_to_listnode(data['list2']))),
                output,
            )


if __name__ == '__main__':
    unittest.main()
