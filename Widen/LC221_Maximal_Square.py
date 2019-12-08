"""
221. Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

# dp
# time complexity -- O(N^2)
# Runtime: 192 ms, faster than 93.66% of Python3 online submissions for Maximal Square.
# Memory Usage: 13.8 MB, less than 90.91% of Python3 online submissions for Maximal Square.
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        n_row, n_col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n_col)] for _ in range(n_row)]
        if matrix[0][0] == 1:
            dp[0][0] = 1
        max_len = 0
        for i in range(n_row):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                max_len = 1
        for j in range(n_col):
            if matrix[0][j] == "1":
                dp[0][j] = 1
                max_len = 1
                
        for i in range(1, n_row):
            for j in range(1, n_col):
                if matrix[i][j] == "0":
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_len = max(max_len, dp[i][j])
        return max_len**2




