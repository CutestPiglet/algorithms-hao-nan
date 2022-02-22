# coding: utf-8

import unittest

from problems.same_tree import Solution
from problems.utils import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            {'p': '[1,2,3]', 'q': '[1,2,3]'},
            {'p': '[1,2]', 'q': '[1,null,2]'},
            {'p': '[1,2]', 'q': '[2,1]'},
            {'p': '[]', 'q': '[]'},
            {'p': '[10]', 'q': '[]'},
        ]
        expected_output = [
            True,
            False,
            False,
            True,
            False,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.isSameTree(deserialize_tree_str(data['p']), deserialize_tree_str(data['q'])), output)


if __name__ == '__main__':
    unittest.main()
