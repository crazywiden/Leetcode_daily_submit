"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""

# method -- use two array to do dp, very clever
# reference: https://www.cnblogs.com/lightwindy/p/8532035.html
# time complexity - O(N)
# space complexity - 0(N) we can further modify this to make it O(1)
# Runtime: 44 ms, faster than 87.66% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
# Memory Usage: 14 MB, less than 13.64% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell
        
