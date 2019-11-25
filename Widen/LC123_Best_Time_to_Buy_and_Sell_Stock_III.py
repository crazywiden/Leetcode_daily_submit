"""
LC123. Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
# brutal force -- TLE
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        res = 0
        for i in range(1, len(prices)+1):
            left_profit = self.cal_profit(prices[:i])
            right_profit = self.cal_profit(prices[i:])
            # print(left_profit, right_profit, i, prices[i])
            res = max(res, left_profit + right_profit)
        return res
    
    def cal_profit(self, arr):
        if len(arr) == 0:
            return 0
        res = 0
        curr_min, curr_max = arr[0], arr[0]
        for i in range(1, len(arr)):
            if arr[i] <= curr_min:
                res = max(res, curr_max - curr_min)
                curr_max = arr[i]
                curr_min = arr[i]
            else:
                curr_max = max(arr[i], curr_max)

        res = max(curr_max-curr_min, res)
        return res


# two array dp
# finnaly!!
# Runtime: 116 ms, faster than 12.79% of Python3 online submissions for Best Time to Buy and Sell Stock III.
# Memory Usage: 18.4 MB, less than 36.36% of Python3 online submissions for Best Time to Buy and Sell Stock III.
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        k = 2
        N = len(prices)
        res = 0
        # define state
        global_profit = [[0 for _ in range(k)] for _ in range(N)]
        local_profit = [[0 for _ in range(k)] for _ in range(N)]
        # update
        for i in range(1, N):
            for j in range(k):
                if j == 0:
                    local_profit[i][j] = max(local_profit[i-1][j]-prices[i-1]+prices[i], 0)
                else:
                    local_profit[i][j] = max(global_profit[i-1][j-1], local_profit[i-1][j])-prices[i-1]+prices[i]
                global_profit[i][j] = max(global_profit[i-1][j], local_profit[i][j])
        return global_profit[-1][-1]



# find min-max interval solution
# Runtime: 72 ms, faster than 98.49% of Python3 online submissions for Best Time to Buy and Sell Stock III.
# Memory Usage: 13.9 MB, less than 72.73% of Python3 online submissions for Best Time to Buy and Sell Stock III.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ### find min-max intervals
        ### if 0: return 0
        ### if 2: return max 2, or break top 1
        ### if 1: break
        
        if not prices: 
            return 0
        
        prices.append(-float('inf'))
        cur_min,cur_max = 0,0
        g_min,g_max = 0,0
        for i in range(1,len(prices)):
            if prices[i]<=prices[cur_min]:
                if prices[cur_max]-prices[cur_min] > prices[g_max]-prices[g_min]:
                    g_max,g_min = cur_max,cur_min
                cur_max,cur_min = i,i
            elif prices[i]>=prices[cur_max]:
                    cur_max = i
        #print(g_max,g_min)
        if prices[g_max]==prices[g_min]: return 0
        
        cur_min,cur_max = 0,0
        g1_min,g1_max = 0,0
        for i in range(1,g_min+1):
            if prices[i]<=prices[cur_min]:
                if prices[cur_max]-prices[cur_min] > prices[g1_max]-prices[g1_min]:
                    g1_max,g1_min = cur_max,cur_min
                cur_max,cur_min = i,i
            elif prices[i]>=prices[cur_max]:
                    cur_max = i
        #print(g1_max,g1_min)
        
        cur_min,cur_max = g_max+1,g_max+1
        g2_min,g2_max = g_max+1,g_max+1
        for i in range(g_max+1,len(prices)):
            if prices[i]<=prices[cur_min]:
                if prices[cur_max]-prices[cur_min] > prices[g2_max]-prices[g2_min]:
                    g2_max,g2_min = cur_max,cur_min
                cur_max,cur_min = i,i
            elif prices[i]>=prices[cur_max]:
                    cur_max = i
        #print(g2_max,g2_min)
        
        gg_max,gg_min = g1_max,g1_min
        if prices[g2_max]-prices[g2_min] > prices[g1_max]-prices[g1_min]:
            gg_max,gg_min = g2_max,g2_min
        #print(gg_max,gg_min)
        
        d_min,d_max = g_min,g_min
        cur_min,cur_max = g_min,g_min
        for i in range(g_min+1,g_max+1):
            if prices[i]<=prices[i-1]:
                cur_min = i
            else:
                if prices[cur_min]-prices[cur_max]<prices[d_min]-prices[d_max]:
                    d_min,d_max = cur_min,cur_max
                cur_min,cur_max = i,i
        #print(d_max,d_min)
        
        return max(prices[g_max]-prices[g_min]+prices[gg_max]-prices[gg_min], prices[d_max]-prices[g_min]+prices[g_max]-prices[d_min])

# a more elegant solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstMin  = secondMin = 999999999
        firstProfit = secondProfit = 0
        
        for price in prices:
            if price < firstMin:
                firstMin = price  
            if price - firstMin > firstProfit:
                firstProfit = price - firstMin 
            if price - firstProfit < secondMin:
                secondMin = price - firstProfit
            if price - secondMin >= secondProfit:
                secondProfit = price - secondMin
        return secondProfit 




# another dp
# Runtime: 88 ms, faster than 68.34% of Python3 online submissions for Best Time to Buy and Sell Stock III.
# Memory Usage: 13.9 MB, less than 72.73% of Python3 online submissions for Best Time to Buy and Sell Stock III.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l = len(prices)
        k = 2
        dp = [[0] * l for _ in range(k+1)]
        for i in range(1, k+1):
            # money spent at first day
            prev = dp[i - 1][0] - prices[0]
            for j in range(1, l):
                # money spent if sell stock today
                deal = prev + prices[j]
                # compare money spent if don't sell stock today with sell stock today
                dp[i][j] = max(dp[i][j - 1], deal)
                # compare i - 1 deals during j days, and don't buy stock today
                # with i - 1 deals during j days, and buy stock today
                prev = max(prev, dp[i - 1][j] - prices[j])
        return dp[-1][-1]
