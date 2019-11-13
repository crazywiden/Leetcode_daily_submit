"""
LC188. Best Time to Buy and Sell Stock IV

Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

# variant of LC123188. Best Time to Buy and Sell Stock III
# but just use my original implementation will TLE
# need to be optimized
class Solution:
    def maxProfit(self, k: int, prices) -> int:
        if len(prices) == 0 or k == 0:
            return 0
        
        N = len(prices)
        res = 0
        # define state
        global_profit = [[0 for _ in range(k)] for _ in range(N)]
        local_profit = [[0 for _ in range(k)] for _ in range(N)]

        # update
        for i in range(1, N):
            diff = prices[i] - prices[i-1]
            for j in range(k):
                if j == 0:
                    local_profit[i][j] = max(local_profit[i-1][j]+diff, 0)
                else:
                    local_profit[i][j] = max(global_profit[i-1][j-1], local_profit[i-1][j])+diff
                global_profit[i][j] = max(global_profit[i-1][j], local_profit[i][j])
                print("local_profit: ", local_profit)
                print("global_profit:", global_profit)
                print("======")
        return global_profit[-1][-1]



# little pruning..
# when k > len(prices)/2, equivalent to can trade as many as you can
# Runtime: 140 ms, faster than 20.68% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
# Memory Usage: 17.4 MB, less than 16.67% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0 or k == 0:
            return 0
        
        N = len(prices)
        if k > N/2:
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
        
            
        res = 0
        # define state
        global_profit = [[0 for _ in range(k)] for _ in range(N)]
        local_profit = [[0 for _ in range(k)] for _ in range(N)]

        # update
        for i in range(1, N):
            diff = prices[i] - prices[i-1]
            for j in range(k):
                if j == 0:
                    local_profit[i][j] = max(local_profit[i-1][j]+diff, 0)
                else:
                    local_profit[i][j] = max(global_profit[i-1][j-1], local_profit[i-1][j])+diff
                global_profit[i][j] = max(global_profit[i-1][j], local_profit[i][j])

        return global_profit[-1][-1]

