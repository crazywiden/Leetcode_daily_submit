"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""

# simple dp
# time complexity -- O(N * max(nums)), TLE
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        if n == 2:
            return 1
        
        dp = [0 for _ in range(n)]
        dp[-2] = 1
        for i in range(n-3, -1, -1):
            tmp = n
            for j in range(1, nums[i]+1):
                if i + j >= n:
                    break
                tmp = min(tmp, dp[i + j])
            dp[i] = 1 + tmp
        return dp[0]

# little optimization 
# Runtime: 112 ms, faster than 26.34% of Python3 online submissions for Jump Game II.
# Memory Usage: 14.8 MB, less than 8.33% of Python3 online submissions for Jump Game II.
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        if n == 2:
            return 1
        
        dp = [0 for _ in range(n)]
        if nums[-2] != 0:
            dp[-2] = 1
        for i in range(n-3, -1, -1):
            tmp = n
            for j in range(nums[i], 0, -1):
                if i + j == n-1:
                    tmp = 0
                    break
                if i+j < n and dp[i+j] != 0:
                    tmp = min(tmp, dp[i+j])
                if tmp == 1:
                    break
            dp[i] = 1 + tmp
            
        return dp[0]
    
