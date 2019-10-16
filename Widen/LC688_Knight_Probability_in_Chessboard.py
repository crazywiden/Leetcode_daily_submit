"""
LC688. Knight Probability in Chessboard
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

 

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
 
"""



# classical dp problem -- 2d dp and memory optimization
# Runtime: 200 ms, faster than 75.56% of Python3 online submissions for Knight Probability in Chessboard.
# Memory Usage: 16.1 MB, less than 61.54% of Python3 online submissions for Knight Probability in Chessboard.
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = {i:[[-1 for _ in range(N)] for _ in range(N)] for i in range(1, K+1)}
        def helper(left_step, row, col):
            
            if row < 0 or row > N-1 or col < 0 or col > N-1:
                return 0
            
            if left_step == 0:
                return 1
            
            if dp[left_step][row][col] != -1:
                return dp[left_step][row][col]
            else:
                prob = helper(left_step-1, row-2, col-1) + helper(left_step-1, row-2, col+1) + helper(left_step-1, row-1, col-2) + helper(left_step-1, row-1, col+2) + helper(left_step-1, row+1, col-2) + helper(left_step-1, row+1, col+2) + helper(left_step-1, row+2, col-1) + helper(left_step-1, row+2, col+1)
                prob = prob / 8
                dp[left_step][row][col] = prob
            return dp[left_step][row][col]
        return helper(K, r, c)
        