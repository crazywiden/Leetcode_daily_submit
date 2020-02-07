"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
"""

# classical dp, relatively easy
# time complexity -- O(N^2)
# space complexity -- O(1)
# Runtime: 60 ms, faster than 18.51% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 14.1 MB, less than 22.22% of Python3 online submissions for Combination Sum IV.
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp.pop()


# add dfs with memeory method
# Runtime: 44 ms, faster than 57.82% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 15.7 MB, less than 22.22% of Python3 online submissions for Combination Sum IV.
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.memo = {} # key is a target, value is num of combination sum of that target
        self.dfs(nums, target)
        return self.memo[target]
    
    def dfs(self, A, target):
        if target < 0:
            return 0
        
        if target in self.memo:
            return self.memo[target]
        
        cnt = 0
        for i in range(len(A)):
            if A[i] == target:
                cnt += 1
            elif A[i] < target:
                cnt += self.dfs(A, target-A[i])
            
        self.memo[target] = cnt
        return cnt


