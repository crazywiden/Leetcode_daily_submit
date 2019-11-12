"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""

# Runtime: 60 ms, faster than 97.99% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Best Time to Buy and Sell Stock II.



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        res = 0
        curr_min, curr_max = prices[0], prices[0]
        for i in range(1, len(prices)):
            if prices[i] < curr_max:
                res += (curr_max - curr_min)
                curr_max, curr_min = prices[i], prices[i]
            else:
                curr_max = prices[i]
        res += (curr_max - curr_min)
        return res