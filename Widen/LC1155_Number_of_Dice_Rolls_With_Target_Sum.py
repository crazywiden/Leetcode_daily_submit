"""
1155. Number of Dice Rolls With Target Sum
"""


# 2d dp
# time complexity -- O(d f target)
# dp[i][j] means the number of method 
# for i dice to achieve j   
# Runtime: 164 ms, faster than 90.36% of Python3 online submissions for Number of Dice Rolls With Target Sum.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Number of Dice Rolls With Target Sum.
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        REMAINDER = 10**9 + 7
        if d > target or d*f < target:
            # this line could make the run time much faster
            return 0
        # dp[i][j] means the number of method 
        # for i dice to achieve j
        dp = [[0 for _ in range(target+1)] for _ in range(d)]
        for i in range(1, min(f, target)+1):
            dp[0][i] = 1
        for i in range(1, d):
            for j in range(i+1, target+1):
                for res in range(max(1, j-f), j):
                    dp[i][j] += dp[i-1][res]
                
        return dp[-1][-1] % REMAINDER
    