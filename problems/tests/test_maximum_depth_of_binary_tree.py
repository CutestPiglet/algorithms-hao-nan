# coding: utf-8

import unittest

from problems.maximum_depth_of_binary_tree import Solution
from problems.utils import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            '[3,9,20,null,null,15,7]',
            '[1,null,2]',
        ]
        expected_output = [
            3,
            2,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.maxDepth(deserialize_tree_str(data)), output)


if __name__ == '__main__':
    unittest.main()
