"""
LC77 combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

# backtracking
# Runtime: 672 ms, faster than 17.95% of Python3 online submissions for Combinations.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Combinations.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        level = 0
        self.dfs(res, [], list(range(1, n+1)), level, k)
        return res
    
    def dfs(self, res, tmp, nums, level, k):
        if level == k:
            res.append(tmp.copy())
            return 
        for i in range(len(nums)):
            tmp.append(nums[i])
            level += 1
            self.dfs(res, tmp, nums[i+1:], level, k)
            level -= 1
            tmp.pop()


# faster version
# Runtime: 540 ms, faster than 58.79% of Python3 online submissions for Combinations.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Combinations.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(res, [], 1, n, k)
        return res
    
    def dfs(self, res, tmp, start, n, k):
        if len(tmp) == k:
            res.append(tmp.copy())
            return 
        for i in range(start, n+1):
            tmp.append(i)
            self.dfs(res, tmp, i+1, n, k)
            tmp.pop()
            