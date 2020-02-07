"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

# Runtime: 88 ms, faster than 47.84% of Python3 online submissions for Combination Sum.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Combination Sum.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(res, [], candidates, target)
        return res
    
    def dfs(self, res, tmp, A, curr_target):
        if curr_target < 0:
            return 
        if curr_target == 0:
            res.append(tmp.copy())
            return 
        for i in range(len(A)):
            tmp.append(A[i])
            self.dfs(res, tmp, A[i:], curr_target - A[i])
            tmp.pop()


