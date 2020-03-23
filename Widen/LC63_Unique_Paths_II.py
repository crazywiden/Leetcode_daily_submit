"""
63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.
"""

# simple dp again
# Runtime: 44 ms, faster than 73.44% of Python3 online submissions for Unique Paths II.
# Memory Usage: 13 MB, less than 93.33% of Python3 online submissions for Unique Paths II.
class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        n_row, n_col = len(A), len(A[0])
        dp = [[0 for _ in range(n_col)] for _ in range(n_row)]
        if A[0][0] == 1:
            return 0
        
        for i in range(n_row):
            if A[i][0] == 1:
                break
            dp[i][0] = 1
        
        for j in range(n_col):
            if A[0][j] == 1:
                break
            dp[0][j] = 1
        
        for i in range(1, n_row):
            for j in range(1, n_col):
                if A[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]