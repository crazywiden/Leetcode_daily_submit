"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
# Runtime: 32 ms, faster than 68.36% of Python3 online submissions for Subsets.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Subsets.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(res, [], nums)
        return res
    
    def dfs(self, res, tmp, nums):
        res.append(tmp.copy())
        for i in range(len(nums)):
            tmp.append(nums[i])
            self.dfs(res, tmp, nums[i+1:])
            tmp.pop()