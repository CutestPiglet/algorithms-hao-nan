# coding: utf-8

import unittest

from problems.linked_list_cycle import Solution1, Solution2
from problems.utils import convert_list_to_listnode


class TestCase(unittest.TestCase):
    def setUp(self):

        self.input_data = [
            {'head': [3, 2, 0, -4], 'pos': 1},
            {'head': [1, 2], 'pos': 0},
            {'head': [1], 'pos': -1},
            {'head': [], 'pos': 0},
        ]
        self.expected_output = [
            True,
            True,
            False,
            False,
        ]

    def test_solution1(self):
        solution = Solution1()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.hasCycle(convert_list_to_listnode(data['head'], data['pos'])), output)

    def test_solution2(self):
        solution = Solution2()
        for data, output in zip(self.input_data, self.expected_output):
            self.assertEqual(solution.hasCycle(convert_list_to_listnode(data['head'], data['pos'])), output)


if __name__ == '__main__':
    unittest.main()
