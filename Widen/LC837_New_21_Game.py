"""
LC 837 -- new 21 game
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278
"""

# dp with memory fails...
# now I am familar with dfs with memory, but still need to work more on dp
# Runtime: 88 ms, faster than 63.41% of Python3 online submissions for New 21 Game.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for New 21 Game.
class Solution:
    def new21Game(self, N, K, W):
        # Write your code here.
        if K == 0 or N >= K + W: 
            return 1.0
        dp = [1.0] + [0.0] * N
        Wsum = 1.0
        for i in range(1, N + 1):
            dp[i] = Wsum / W
            if i < K: 
                Wsum += dp[i]
            if i - W >= 0: 
                Wsum -= dp[i - W]
        return sum(dp[K:])