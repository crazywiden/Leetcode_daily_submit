"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
"""

# interval dp
# be careful about the edge case when update dp 
# Runtime: 772 ms, faster than 57.54% of Python3 online submissions for Guess Number Higher or Lower II.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower II.
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for i in range(n+1, 0, -1):
            for j in range(i+1, n+1):
                tmp = float("inf")
                for k in range(i, j+1):
                    if k == i:
                        tmp = min(tmp, k + dp[k+1][j])
                    elif k == j:
                        tmp = min(tmp, k + dp[i][k-1])
                    else:
                        tmp = min(tmp, k+max(dp[i][k-1], dp[k+1][j]))
                dp[i][j] = tmp
        return dp[1][n]
    