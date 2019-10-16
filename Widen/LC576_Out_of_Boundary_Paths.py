"""
LC576 -- Out of Boundary Paths
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, 
you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). 
However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. 
The answer may be very large, return it after mod 109 + 7.
"""

# almost the same as Kight Chessborad
# one more pruning: when step < min(row, m-row, col, n-col) return 0
# Runtime: 216 ms, faster than 45.75% of Python3 online submissions for Out of Boundary Paths.
# Memory Usage: 16.7 MB, less than 33.33% of Python3 online submissions for Out of Boundary Paths.

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = {step:[[0 for _ in range(n)] for _ in range(m)] for step in range(1, N+1)}
        def helper(row, col, step):
            if (row < 0 or row > m-1 or col < 0 or col > n-1) and step >= 0:
                return 1
            
            if step == 0:
                return 0
            
            dist = min(row, m-row, col, n-col)
            if step < dist:
                return 0
            
            if dp[step][row][col] != 0:
                return dp[step][row][col]
            cnt = helper(row+1, col, step-1) + helper(row-1, col, step-1) + helper(row, col+1, step-1) + helper(row, col-1, step-1)
            dp[step][row][col] = cnt
            return cnt
        res = helper(i, j, N)
        return res % (7 + 10**9)