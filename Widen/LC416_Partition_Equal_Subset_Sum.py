"""
LC416 Partition Equal Subset Sum
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""

# dp solution
# time complexity -- O(n*sum(nums))
# Runtime: 3360 ms, faster than 11.09% of Python3 online submissions for Partition Equal Subset Sum.
# Memory Usage: 18 MB, less than 13.54% of Python3 online submissions for Partition Equal Subset Sum.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        S = sum(nums)
        if S % 2 != 0:
            return False
        target = S // 2
        
        dp = [[False for _ in range(target+1)] for _ in range(n+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            dp[i][0] = True
            if nums[i-1] > target:
                return False
        for i in range(1, n+1):
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j]
                if j < nums[i-1]:
                    continue
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i][j]
        
        for i in range(1, n+1):
            if dp[i][-1]:
                return True
        return False


# first try -- dfs
# time complexity -- O(N^2)
# space complexity -- O(N)
# TLE on len(nums) == 99
class Solution:
    def canPartition(self, nums) -> bool:
        if len(nums) == 0:
            return False
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        def dfs(target, nums):
            if target == 0:
                return True
            if target < 0:
                return False
            for i in range(len(nums)):
                tmp_num = nums[:i] + nums[i+1:]
                if dfs(target-nums[i], tmp_num):
                    return True
            return False
        
        return dfs(target, nums)

# method 2
# check each element individually in advance...
# then passed all test case...
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        def dfs(target, nums):
            if target == 0:
                return True
            if target < 0:
                return False
            
            for i in range(len(nums)-1, -1, -1):
                tmp_num = nums[:i] + nums[i+1:]
                if dfs(target-nums[i], tmp_num):
                    return True
            return False
        for i in range(len(nums)):
            if nums[i] > target:
                return False
            if nums[i] == target:
                return True
        return dfs(target, nums)



