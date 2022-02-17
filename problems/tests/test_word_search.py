# coding: utf-8

import unittest

from problems.word_search import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            {'board': [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'word': 'ABCCED'},
            {'board': [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'word': 'SEE'},
            {'board': [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'word': 'ABCB'},
        ]
        expected_output = [
            True,
            True,
            False,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.exist(data['board'], data['word']), output)


if __name__ == '__main__':
    unittest.main()
