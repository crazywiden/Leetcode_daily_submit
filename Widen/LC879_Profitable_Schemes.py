"""
879. Profitable Schemes
There are G people in a gang, and a list of various crimes they could commit.

The i-th crime generates a profit[i] and requires group[i] gang members to participate.

If a gang member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least P profit, and the total number of gang members participating in that subset of crimes is at most G.

How many schemes can be chosen?  Since the answer may be very large, return it modulo 10^9 + 7.

 

Example 1:

Input: G = 5, P = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: 
To make a profit of at least 3, the gang could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
Example 2:

Input: G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: 
To make a profit of at least 5, the gang could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
"""
# optimized version
# time complexity -- O(N*G*P)
# space complexity -- O(G*P)
class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        n = len(group)
        MOD = 10**9 + 7
        dp = [[[0 for _ in range(P+1)] for _ in range(G+1)] for _ in range(2)]
        old, new = 1, 0
        dp[new][0][0] = 1
        
        for i, (people, gain) in enumerate(zip(group, profit)):
            old, new = new, 1-new
            for g in range(G+1):
                for p in range(P+1):
                    dp[new][g][p] = dp[old][g][p]
                    if g < people:
                        continue
                    dp[new][g][p] += dp[old][g-people][max(0, p-gain)] % MOD
        res = 0
        for i in range(G+1):
            res += dp[new][i][P] % MOD
        return res % MOD

# 3d dp 
# time complexity -- O(N*G*P)
# space complexity -- O(N*G*P)
class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        n = len(group)
        MOD = 10**9 + 7
        dp = [[[0 for _ in range(P+1)] for _ in range(G+1)] for _ in range(n+1)]
        dp[0][0][0] = 1
        
        for i, (people, gain) in enumerate(zip(group, profit)):
            for g in range(G+1):
                for p in range(P+1):
                    dp[i+1][g][p] = dp[i][g][p]
                    if g < people:
                        continue
                    dp[i+1][g][p] += dp[i][g-people][max(0, p-gain)] % MOD
        res = 0
        for i in range(G+1):
            res += dp[n][i][P] % MOD
        return res % MOD
