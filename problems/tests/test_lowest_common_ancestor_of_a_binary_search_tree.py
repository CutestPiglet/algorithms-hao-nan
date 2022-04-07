# coding: utf-8

import unittest

from problems.lowest_common_ancestor_of_a_binary_search_tree import Solution
from problems.utils import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            {'root': '[6,2,8,0,4,7,9,null,null,3,5]', 'p': '[2]', 'q': '[8]'},
            {'root': '[6,2,8,0,4,7,9,null,null,3,5]', 'p': '[2]', 'q': '[4]'},
            {'root': '[2,1]', 'p': '[2]', 'q': '[1]'},
        ]
        expected_output = [
            '[6]',
            '[2]',
            '[2]',
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(
                self.solution.lowestCommonAncestor(
                    deserialize_tree_str(data['root']),
                    deserialize_tree_str(data['p']),
                    deserialize_tree_str(data['q']),
                ).val,
                deserialize_tree_str(output).val,
            )


if __name__ == '__main__':
    unittest.main()
