"""
LC 935 -- Knight Dialer
A chess knight can move as indicated in the chess diagram below:

This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.

 
"""


# too simple
# Runtime: 476 ms, faster than 84.22% of Python3 online submissions for Knight Dialer.
# Memory Usage: 13.8 MB, less than 23.53% of Python3 online submissions for Knight Dialer.

class Solution:
    def knightDialer(self, N: int) -> int:
        dp = [1 for _ in range(10)]
        if N == 1:
            return sum(dp)
        for i in range(N-1):
            new_dp = dp.copy()
            new_dp[0] = dp[4] + dp[6]
            new_dp[1] = dp[6] + dp[8]
            new_dp[2] = dp[7] + dp[9]
            new_dp[3] = dp[4] + dp[8]
            new_dp[4] = dp[3] + dp[9] + dp[0]
            new_dp[6] = dp[1] + dp[7] + dp[0]
            new_dp[7] = dp[2] + dp[6]
            new_dp[8] = dp[1] + dp[3]
            new_dp[9] = dp[2] + dp[4]
            dp = new_dp.copy()
        return (sum(dp) - 1) % (10**9 + 7)


# dfs solution
# Runtime: 3016 ms, faster than 10.41% of Python3 online submissions for Knight Dialer.
# Memory Usage: 41 MB, less than 5.88% of Python3 online submissions for Knight Dialer.
class Solution:
    def knightDialer(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 10
        
        graph = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        self.memo = {}
        MOD = 10**9 + 7
        res = 0
        for key in graph:
            res += self.dfs(graph, key, N-1)
        return res % MOD

    def dfs(self, graph, key, step):
        if step == 0:
            return 1
        if (key, step) in self.memo:
            return self.memo[(key, step)]
        res = 0
        for nxt in graph[key]:
            res += self.dfs(graph, nxt, step-1)
        self.memo[(key, step)] = res
        return res
    
