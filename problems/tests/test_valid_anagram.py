# coding: utf-8

import unittest

from problems.valid_anagram import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            {'s': 'anagram', 't': 'nagaram'},
            {'s': 'rat', 't': 'car'},
            {'s': 'aa', 't': 'a'},
            {'s': 'caaa', 't': 'ccaa'},
        ]
        expected_output = [
            True,
            False,
            False,
            False,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.isAnagram(data['s'], data['t']), output)


if __name__ == '__main__':
    unittest.main()
