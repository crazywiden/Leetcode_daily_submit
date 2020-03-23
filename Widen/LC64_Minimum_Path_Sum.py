"""
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

# simple dp again
# Runtime: 96 ms, faster than 90.54% of Python3 online submissions for Minimum Path Sum.
# Memory Usage: 14.4 MB, less than 75.44% of Python3 online submissions for Minimum Path Sum.
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        dp = [[0 for _ in range(n_col)] for _ in range(n_row)]
        dp[0][0] = grid[0][0]
        for i in range(1, n_col):
            dp[0][i] = dp[0][i-1] + grid[0][i]
            
        for i in range(1, n_row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for i in range(1, n_row):
            for j in range(1, n_col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]