# coding: utf-8

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buying_price, max_profit = prices[0], 0

        for selling_price in prices[1:]:
            profit = selling_price - buying_price
            if profit > max_profit:
                max_profit = profit
            else:
                buying_price = min(buying_price, selling_price)

        return max_profit
