"""
LC 329 Longest Increasing Path in a Matrix
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

# met this problem in an interview... But clearly I failed...
# just dp and dfs, nothing special...don't know why I failed...
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        res = -1
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def is_legal(x, y):
            return (x>=0 and x<=n-1 and y>=0 and y<=m-1)
        def helper(x, y):
            if not is_legal(x, y):
                return 0
            if dp[x][y] != 0:
                return dp[x][y]
            res = 1
            for direction in directions:
                next_x = x + direction[0]
                next_y = y + direction[1]
                if is_legal(next_x, next_y) and matrix[next_x][next_y] > matrix[x][y]:
                    tmp_res = helper(next_x, next_y)
                    res = max(tmp_res + 1, res)
            dp[x][y] = res
            return dp[x][y]
        for i in range(n):
            for j in range(m):
                tmp_res = helper(i, j)
                res = max(res, tmp_res)
        return res