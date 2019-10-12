"""
LC494 Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

"""

# method 1 -- dp
# dp[i][j] means number of ways to get j using data nums[:i]
# Runtime: 424 ms, faster than 28.60% of Python3 online submissions for Target Sum.
# Memory Usage: 14.2 MB, less than 50.00% of Python3 online submissions for Target Sum.

# possible optimization way: change hasp map to list
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        all_sum = sum(nums)
        if all_sum < S:
            return 0
        dp = {i:0 for i in range(-all_sum, all_sum+1)}
        possible = {-nums[0], nums[0]}
        
        if nums[0] == 0:
            dp[-nums[0]], dp[nums[0]] = 2, 2
        else:
            dp[-nums[0]], dp[nums[0]] = 1, 1
            
        for i in range(1, len(nums)):
            new_possible = set()
            new_dp = {i:0 for i in range(-all_sum, all_sum+1)}
            for num in possible:
                new_dp[num + nums[i]] += dp[num]
                new_dp[num - nums[i]] += dp[num]
                new_possible.update([num + nums[i], num - nums[i]])
            possible = new_possible.copy()
            dp = new_dp.copy()
        return dp[S]

# method 2: don't understand so far
# Runtime: 80 ms, faster than 96.75% of Python3 online submissions for Target Sum.
# Memory Usage: 13.9 MB, less than 58.33% of Python3 online submissions for Target Sum.
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], t: int) -> int:
        d = sum(nums)-t
        if d < 0 or d%2: return 0
        d //= 2
        dp = [1] + [0]*d
        for n in nums:
            for i in range(d,n-1,-1):
                dp[i] += dp[i-n]
        return dp[d]
                