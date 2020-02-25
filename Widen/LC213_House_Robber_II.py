"""
213. House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""

# Runtime: 20 ms, faster than 99.21% of Python3 online submissions for House Robber II.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for House Robber II.
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 3:
            return max(nums)
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
    
    def helper(self, arr):
        n = len(arr)
        if n <= 2:
            return 0
        dp = [0 for _ in range(n)]
        dp[0] = arr[0]
        dp[1] = arr[1]
        dp[2] = arr[2] + arr[0]
        for i in range(3, n):
            dp[i] = max(dp[i-2], dp[i-3]) + arr[i]
        return max(dp[-1], dp[-2])
            