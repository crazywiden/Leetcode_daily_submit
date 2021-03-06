"""
LC523 --  Continuous Subarray Sum
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
"""

# solution is simple, just dp, very similar to Ones and Zeros
# however, the corner cases in the problem are extremly annoying...
# pay attention to the case when we met zero
# Runtime: 240 ms, faster than 97.32% of Python3 online submissions for Continuous Subarray Sum.
# Memory Usage: 14 MB, less than 14.29% of Python3 online submissions for Continuous Subarray Sum.
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        if N == 0:
            return False
        dp = {0:-1}
        running_sum = 0
        for i in range(N):
            running_sum += nums[i]
            if k == 0:
                remainder = running_sum
            else:
                remainder = running_sum % k
            if remainder not in dp:
                dp[remainder] = i
            elif dp[remainder] + 1 < i:
                return True
        return False
        
# Runtime: 224 ms, faster than 82.38% of Python3 online submissions for Continuous Subarray Sum.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Continuous Subarray Sum.
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        if len(nums) < 2:
            return False
        
        fast_sum = nums[0] + nums[1]
        low_sum = 0
        remainders = set([])
        for i in range(2, len(nums)):
            fast_sum += nums[i]
            low_sum += nums[i-2]
            if k != 0:
                remainders.add(low_sum % k)
                tmp = fast_sum % k
                if tmp in remainders:
                    return True
            elif fast_sum == low_sum:
                return True
        
        if k == 0:
            if fast_sum == 0:
                return True
            return False
        elif fast_sum % k == 0:
            return True
        return False



