"""
LC877 Stone Game
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 

Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""

# revisit -- dp
# Runtime: 904 ms, faster than 17.15% of Python3 online submissions for Stone Game.
# Memory Usage: 19.7 MB, less than 50.00% of Python3 online submissions for Stone Game.
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        if N <= 2:
            return True
        
        dp = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            dp[i][i] = piles[i]
        for i in range(N-1):
            dp[i][i+1] = max(piles[i], piles[i+1])
        
        for i in range(N-2, -1, -1):
            for j in range(i+2, N):
                take_left = min(dp[i+1][j-1], dp[i+2][j]) + piles[i]
                take_right = min(dp[i+1][j-1], dp[i][j-2]) + piles[j]
                dp[i][j] = max(take_left, take_right)
            
        return dp[0][-1]*2 >= sum(piles)
                
        

# this one is exactly the same as LC464 Can I win
# method 1:  minMax strategy
# Runtime: 676 ms, faster than 21.20% of Python3 online submissions for Stone Game.
# Memory Usage: 31.5 MB, less than 25.00% of Python3 online submissions for Stone Game.

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def helper(left, right):
            if left == right:
                return piles[left]
            if left > right:
                return piles[right]
            if dp[left][right] != -1:
                return dp[left][right]
            take_left = piles[left] + min(helper(left+2, right), helper(left+1, right-1))
            take_right = piles[right] + min(helper(left+1, right-1), helper(left, right-2))
            dp[left][right] = max(take_left, take_right)
            return dp[left][right]
        N = len(piles)
        if N == 1:
            return True
        dp = [[-1 for _ in range(N)] for _ in range(N)]
        all_stone = helper(0, N-1)
        return all_stone*2 > sum(piles)



# mathematically... Alex always win...
# in this senario, 
#Alex clearly always wins the 2 pile game. With some effort, we can see that she always wins the 4 pile game.

# If Alex takes the first pile initially, she can always take the third pile. 
# If she takes the fourth pile initially, she can always take the second pile. 
# At least one of first + third, second + fourth is larger, so she can always win.

# We can extend this idea to N piles. Say the first, third, fifth, seventh, etc. piles are white, and the second, fourth, sixth, eighth, etc. piles are black. Alex can always take either all white piles or all black piles, and one of the colors must have a sum number of stones larger than the other color.

# Hence, Alex always wins the game.

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True