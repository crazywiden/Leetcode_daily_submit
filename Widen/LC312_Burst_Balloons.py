"""
312. Burst Balloons
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""

# interval dp
# bug-free code!
# Runtime: 484 ms, faster than 57.05% of Python3 online submissions for Burst Balloons.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Burst Balloons.
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        n = n + 2
        # dp[i][j] is the result of nums[i...j] all bursted 
        # while nums[i] and nums[j] don't 
        dp = [[0 for _ in range(n)] for _ in range(n)]
        nums = [1] + nums + [1]
        for i in range(n, -1, -1):
            for j in range(i+2, n):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
        return dp[0][-1]
        
        