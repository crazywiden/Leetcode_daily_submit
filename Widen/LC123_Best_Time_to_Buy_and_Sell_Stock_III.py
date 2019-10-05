"""
LC 123 -- Best Time to buy and sell stock III
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
# method1 -- dp
# 
# Runtime: 76 ms, faster than 97.91% of Python3 online submissions for Best Time to Buy and Sell Stock III.
# Memory Usage: 14.7 MB, less than 63.64% of Python3 online submissions for Best Time to Buy and Sell Stock III.
# reference: https://www.cnblogs.com/lightwindy/p/8531947.html



# method1 -- divide and conquer algorithm to solve instead of dp
# genius!!
# Runtime: 76 ms, faster than 97.91% of Python3 online submissions for Best Time to Buy and Sell Stock III.
# Memory Usage: 14.7 MB, less than 63.64% of Python3 online submissions for Best Time to Buy and Sell Stock III.
# reference: https://www.cnblogs.com/lightwindy/p/8531947.html
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold1, hold2 = float("-inf"), float("-inf")
        release1, release2 = 0, 0
        for i in prices:
            release2 = max(release2, hold2 + i)
            hold2    = max(hold2,    release1 - i)
            release1 = max(release1, hold1 + i)
            hold1    = max(hold1,    -i);
        return release2