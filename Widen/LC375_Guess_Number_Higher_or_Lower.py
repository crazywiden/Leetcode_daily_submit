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

# this is a wrong solution but don't know where is wrong...
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n == 1:
            return 0
        
        dp = [n*n for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1
        # first create dp
        for i in range(3, n+1):
            for j in range(1, i+1):
                if j >= i - 1:
                    dp[i] = min(dp[i], j + dp[j-1])

                else:
                    dp[i] = min(dp[i], j + max(dp[j-1], dp[i-j]+j))
                
        min_cost = n*n
        for i in range(1, n+1):
            if i >= n - 1:
                min_cost = min(min_cost, i + dp[i-1])
            left_cost = dp[i-1]
            right_cost = dp[n-i] + i
            tmp_cost = i + max(left_cost, right_cost)
            min_cost = min(tmp_cost, min_cost)
        return min_cost



# right solution -- 2d dp
# reference: https://www.csdn.net/link?target_url=https%3A%2F%2Fwww.hrwhisper.me%2Fleetcode-guess-number-higher-lower-ii%2F&id=82893656&token=fe5c413665b21f92aa39cb6c968c9fb4
# Runtime: 544 ms, faster than 84.23% of Python3 online submissions for Guess Number Higher or Lower II.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower II.
# dp[i][j] means lowest cost of searching between i and j
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for l in range(n - 1, 0, -1):
            for r in range(l + 1, n + 1):
                dp[l][r] = min(i + max(dp[l][i - 1], dp[i + 1][r]) for i in range(l, r))
        return dp[1][n]