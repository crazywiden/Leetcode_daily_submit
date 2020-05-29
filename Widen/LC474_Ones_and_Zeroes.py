"""
474. Ones and Zeroes
Given an array, strs, with strings consisting of only 0s and 1s. Also two integers m and n.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10","0001","1","0".
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
"""

# Knapsack problem
# be careful about the update order of dp
# time complexity --- O(len(strs) * m * n)
# Runtime: 3424 ms, faster than 59.80% of Python3 online submissions for Ones and Zeroes.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Ones and Zeroes.
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def get_zero_one(s):
            freq = collections.Counter(s)
            return freq['0'], freq['1']
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for s in strs:
            zero, one = get_zero_one(s)
            if zero > m or one > n:
                continue
            for i in range(n, one-1, -1):
                for j in range(m, zero-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-one][j-zero]+1)

        return dp[-1][-1]



# backtracking -- TLE
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)
        freqs = [collections.Counter(s) for s in strs]
        nums = [[item['0'], item['1']] for item in freqs]
        visited = "0" * N  # visited[i] == "0" means didn't visited
        self.memo = {}
        return self.dfs(m, n, nums, visited, 0)
    
    def dfs(self, target_zero, target_one, nums, visited, cnt):
        if visited == "1" * len(nums):
            return cnt
        if target_zero == 0 and target_one == 0:
            return cnt
        if (visited, target_zero, target_one) in self.memo:
            return self.memo[(visited, target_zero, target_one)]
        base = 0
        for i in range(len(nums)):
            if visited[i] == "1":
                continue
            curr_zero, curr_one = nums[i]
            if curr_zero > target_zero or curr_one > target_one:
                continue
            visited = visited[:i] + "1" + visited[i+1:]
            tmp = self.dfs(target_zero-curr_zero, target_one-curr_one, nums, visited, 1)
            visited = visited[:i] + "0" + visited[i+1:]
            base = max(tmp, base)

        cnt += base
        self.memo[(visited, target_zero, target_one)] = cnt
        return cnt
    
        
        
        
        