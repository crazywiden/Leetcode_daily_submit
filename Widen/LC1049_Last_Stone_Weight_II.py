"""
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)
"""



# classical 0/1 knapsack problem
# 2d dp
# Runtime: 68 ms, faster than 19.40% of Python3 online submissions for Last Stone Weight II.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Last Stone Weight II.
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        tot_sum = sum(stones)
        half_sum = tot_sum // 2
        N = len(stones)
        dp = [[0 for _ in range(half_sum+1)] for _ in range(N)]
        for i in range(half_sum+1):
            if stones[0] <= i:
                dp[0][i] = stones[0]
        
        for i in range(1, N):
            for j in range(half_sum+1):
                if stones[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i]] + stones[i])
        return tot_sum - 2*dp[N-1][half_sum]




# use a faster method
# use 1d dp
# Runtime: 32 ms, faster than 97.68% of Python3 online submissions for Last Stone Weight II.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Last Stone Weight II.
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        tot_sum = sum(stones)
        half_sum = tot_sum // 2
        N = len(stones)
        dp = [False for _ in range(half_sum + 1)]
        dp[0] = True
        # if stones[0]<=half_sum:
        #     dp[stones[0]] = True
            
        for i in range(N):
            for j in range(half_sum, stones[i]-1, -1):
                dp[j] = dp[j] or dp[j-stones[i]]
        for i in range(half_sum, -1, -1):
            if dp[i]:
                return tot_sum - 2*i
        return 0
        
        





