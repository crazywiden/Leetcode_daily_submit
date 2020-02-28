"""
1262. Greatest Sum Divisible by Three
Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
"""

# actually should be dp
# but dp is much slower than this version
# Runtime: 272 ms, faster than 87.30% of Python3 online submissions for Greatest Sum Divisible by Three.
# Memory Usage: 17.7 MB, less than 100.00% of Python3 online submissions for Greatest Sum Divisible by Three.
import heapq
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        tot_sum = sum(nums)
        remainder = tot_sum % 3
        if remainder == 0:
            return tot_sum
        single_min = float("inf")
        double_min = []
        is_seen = False
        for i in range(n):
            if nums[i] % 3 == 3-remainder:
                heapq.heappush(double_min, -nums[i])
                if len(double_min) > 2:
                    heapq.heappop(double_min)
            if nums[i] % 3 == remainder:
                single_min = min(single_min, nums[i])
                is_seen = True
        res = 0
        if is_seen:
            res = max(res, tot_sum-single_min)
        if len(double_min) == 2:
            res = max(res, tot_sum + sum(double_min))
        return res

# dp solution
# notice the use of "for ele in dp[:]" hail Python!!
# Runtime: 408 ms, faster than 56.25% of Python3 online submissions for Greatest Sum Divisible by Three.
# Memory Usage: 17.7 MB, less than 100.00% of Python3 online submissions for Greatest Sum Divisible by Three.
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp[i] is the maximum number that can be achieved when remainder==3
        dp = [0, 0, 0]  
        for num in nums:
            for ele in dp[:]:
                dp[(ele+num)%3] = max(dp[(ele+num)%3], ele+num)
        return dp[0]

        
            
        