"""
LC714 -- Best Time to Buy and Sell Stock with Transaction Fee
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
"""


# same as LC309, but this time we do without cooldown
# time complexity - O(N)
# space complexity - 0(1)
# Runtime: 824 ms, faster than 52.45% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
# Memory Usage: 20.7 MB, less than 12.50% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        buy, sell = -prices[0], 0
        for i in range(1, len(prices)):
            buy = max(buy, sell - prices[i])
            sell = max(buy + prices[i] - fee, sell)
        return sell