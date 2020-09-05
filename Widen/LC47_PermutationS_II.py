"""
LC47 permutations
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

# revisit
# Runtime: 60 ms, faster than 72.26% of Python3 online submissions for Permutations II.
# Memory Usage: 14 MB, less than 68.00% of Python3 online submissions for Permutations II.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tmp_nums = nums[:i] + nums[i+1:]
            for tmp_res in self.helper(tmp_nums):
                res.append([nums[i]] + tmp_res)
        return res
    
    def helper(self, nums):
        if len(nums) <= 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tmp_nums = nums[:i] + nums[i+1:]
            for tmp_res in self.helper(tmp_nums):
                res.append([nums[i]] + tmp_res)
        return res


# Runtime: 48 ms, faster than 93.42% of Python3 online submissions for Permutations II.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Permutations II.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set([])
        self.dfs(res, [], nums, visited)
        return res
    
    def dfs(self, res, tmp, nums, visited):
        if len(visited) == len(nums):
            res.append(tmp.copy())
            return
        start = set([])
        for i in range(len(nums)):
            if i in visited:
                continue
            if nums[i] in start:
                continue
            start.add(nums[i])
            
            tmp.append(nums[i])
            visited.add(i)
            self.dfs(res, tmp, nums, visited)
            visited.remove(i)
            tmp.pop()
            