"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


# backtracking
# Runtime: 48 ms, faster than 44.01% of Python3 online submissions for Subsets II.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Subsets II.
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(depth, start, valuelist):
            if valuelist not in ans:
                ans.append(valuelist)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth + 1, i + 1, valuelist + [nums[i]])

        nums.sort()
        ans = []
        dfs(0, 0, [])
        return ans