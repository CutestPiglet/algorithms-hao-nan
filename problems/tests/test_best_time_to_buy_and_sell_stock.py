# coding: utf-8

import unittest

from problems.best_time_to_buy_and_sell_stock import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        input_data = [
            [7, 1, 5, 3, 6, 4],
            [7, 6, 4, 3, 1],
            [8],
        ]
        expected_output = [
            5,
            0,
            0,
        ]
        for data, output in zip(input_data, expected_output):
            self.assertEqual(self.solution.maxProfit(data), output)


if __name__ == '__main__':
    unittest.main()
