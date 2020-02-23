"""
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

# dp with memeory optimized
# Runtime: 28 ms, faster than 74.42% of Python3 online submissions for House Robber.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for House Robber.
class Solution:
    def rob(self, A: List[int]) -> int:
        n = len(A)
        if n == 0:
            return 0
        if n <= 2:
            return max(A)
        
        prev_three = A[0]
        prev_two = A[1]
        prev_one = A[0] + A[2]
        if n == 3:
            return max(prev_one, prev_two)
        
        res = 0
        for i in range(3, n):
            curr = max(prev_three, prev_two) + A[i]
            res = max(curr, prev_one)
            prev_three = prev_two
            prev_two = prev_one
            prev_one = curr 
        return res
        
# original dp
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0 
        if n <= 2:
            return max(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]
        for i in range(3, n):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        return max(dp[-2], dp[-1])