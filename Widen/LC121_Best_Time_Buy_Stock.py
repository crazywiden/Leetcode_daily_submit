"""
LC121 -- Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
# time complexity -- O(N)
# space complexity -- O(1)
# Runtime: 76 ms, faster than 53.86% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 14.6 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_price, max_price = prices[0], prices[0]
        diff = 0
        for i in range(1, len(prices)):
            if prices[i] > max_price:
                max_price = prices[i]
                diff = max(diff, max_price - min_price)
            elif prices[i] < min_price:
                max_price, min_price = prices[i], prices[i]
        return diff

# Runtime: 64 ms, faster than 97.11% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 13.9 MB, less than 86.21% of Python3 online submissions for Best Time to Buy and Sell Stock.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_so_far = prices[0]
        min_so_far = prices[0]
        rtn = 0
        for i in range(1, len(prices)):
            if prices[i] < min_so_far:
                rtn = max(rtn, max_so_far - min_so_far)
                min_so_far = prices[i]
                max_so_far = prices[i]
            else:
                max_so_far = max(max_so_far, prices[i])
        rtn = max(rtn, max_so_far-min_so_far)
        return rtn
        
