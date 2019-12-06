"""
1223. Dice Roll Simulation
A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times. 

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls.

Two sequences are considered different if at least one element differs from each other. Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
Example 2:

Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30
Example 3:

Input: n = 3, rollMax = [1,1,1,2,2,3]
Output: 181
 

Constraints:

1 <= n <= 5000
rollMax.length == 6
1 <= rollMax[i] <= 15
Accepted
"""


# my solution 
# not working because recursion depth is reached
# only works when n=2, rollMax = [1,1,1,1,1,1]
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.combination = {}
        self.factorial = {}
        return int(self.helper(n, 0, rollMax))
    
    def helper(self, n, curr_num, curr_max):
        if n == 1:
            return 6-curr_num-1
        if curr_num >= 6:
            return 0
        if curr_max[curr_num] == 0:
            curr_num += 1
            # print(curr_num, curr_max)
            return self.helper(n, curr_num, curr_max)

        cnt = 0
        tot_num = curr_max[curr_num]
        for i in range(tot_num,-1,-1):
            curr_max[curr_num] = i
            cnt += self.choose_n_k(n, i) * self.helper(n-i, curr_num, curr_max)

        return cnt
    
    def choose_n_k(self, n, k):
        if k == 0:
            return 1
        if (n, k) in self.combination:
            return self.combination[(n, k)]
        res = self.cal_fact(n)/(self.cal_fact(k) * self.cal_fact(n-k))
        self.combination[(n, k)] = res
        return res
    
    def cal_fact(self, n):
        if n == 0:
            return 1
        if n in self.factorial:
            return self.factorial[n]
        res = 1
        for i in range(1, n+1):
            res *= i
        self.factorial[n] = res
        return res


# https://coordinate.wang/index.php/archives/2673/
# have the same idea as mine, but I lack of implementation ability
# Runtime: 2212 ms, faster than 22.05% of Python3 online submissions for Dice Roll Simulation.
# Memory Usage: 191.4 MB, less than 100.00% of Python3 online submissions for Dice Roll Simulation.
from functools import lru_cache
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        @lru_cache(None)
        def dfs(n, pre, k):
            if n == 0:
                return 1
            res = 0
            for i in range(6):
                if i == pre and k == rollMax[i]:
                    continue
                res = (res + dfs(n - 1, i, k + 1 if i == pre else 1))%(10**9 + 7)
            return res
        return dfs(n, -1, 0)


# also can run 3d-dp
# reference: https://www.acwing.com/solution/LeetCode/content/5270/
# dp[i][j][k] -- number of combinations in i-th throw, number we got is j, appears k times previously
# dp[i][j][k] = dp[i-1][t][k-1], if j == t
# dp[i][j][k] = \sum_{t \ne j}\sum_{k=1}^{rollMax[t]} dp[i-1][t][k]
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MAX_INT = 10**9 + 7
        dp = [[[0 for _ in range(max(rollMax)+1)] for _ in range(6)] for _ in range(n)]
        for i in range(6):
            dp[0][i][1] = 1
        
        for i in range(1, n):
            for j in range(6):
                for t in range(6):
                    if t == j:
                        for k in range(2, rollMax[j]+1):
                            dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1]) % MAX_INT
                    else:
                        for k in range(1, rollMax[t]+1):
                            dp[i][j][1] = (dp[i][j][1] + dp[i-1][t][k]) % MAX_INT
        ans = 0
        for j in range(6):
            for k in range(1, max(rollMax)+1):
                ans += dp[n-1][j][k]
        return ans % MAX_INT
        







            