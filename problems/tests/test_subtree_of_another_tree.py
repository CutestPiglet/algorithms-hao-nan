# coding: utf-8

import unittest

from problems.subtree_of_another_tree import Solution
from problems.utils import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            {'root': '[3,4,5,1,2]', 'subRoot': '[4,1,2]'},
            {'root': '[3,4,5,1,2,null,null,null,null,0]', 'subRoot': '[4,1,2]'},
            {'root': '[1,1]', 'subRoot': '[1]'},
            {'root': '[3,4,5,1,2]', 'subRoot': '[5]'},
            {'root': '[3,4,5,1,2,null,null,null,null,0]', 'subRoot': '[5]'},
        ]
        expected_output = [
            True,
            False,
            True,
            True,
            True,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.isSubtree(deserialize_tree_str(data['root']), deserialize_tree_str(data['subRoot'])), output)


if __name__ == '__main__':
    unittest.main()
