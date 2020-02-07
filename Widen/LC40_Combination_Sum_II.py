"""
LC40 combination sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
# a little hard because of the existence of duplicate candidates
# this solution is to use tuple to cope with the issue
# but should have more subtle solution
# Runtime: 664 ms, faster than 7.39% of Python3 online submissions for Combination Sum II.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Combination Sum II.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = set([])
        self.dfs(res, [], candidates, target)
        return [list(t) for t in res]
    
    def dfs(self, res, tmp, A, target):
        if target < 0:
            return 
        if target == 0:
            tmp = tuple(sorted(tmp))
            if tmp not in res:
                res.add(tmp)
            return 
        
        for i in range(len(A)):
            tmp.append(A[i])
            self.dfs(res, tmp, A[i+1:], target - A[i])
            tmp.pop()
            

# modify a little
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        self.dfs(res, [], candidates, target)
        return res
    
    def dfs(self, res, tmp, A, target):
        if target < 0:
            return 
        if target == 0:
            res.append(tmp.copy())
            return 
        
        for i in range(len(A)):
            if i > 0 and A[i] == A[i-1]:  # here is the modification
                continue
            tmp.append(A[i])
            self.dfs(res, tmp, A[i+1:], target - A[i])
            tmp.pop()
            
        

        