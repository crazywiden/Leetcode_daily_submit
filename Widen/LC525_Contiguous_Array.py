"""
LC 525 -- Contiguous Array
Description:
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""

# method 1 -- dp
# time complexity -- O(N^2)
# space complexity -- O(N^2)
# failed: TLE at 32/555
# class Solution:
#     def findMaxLength(self, nums) -> int:
#         if len(nums) <= 1:
#             return 0
#         n = len(nums)
#         dp = [[0 for _ in range(n)] for _ in range(n)]
        
#         for i in range(n):
#             dp[i][i] = nums[i]
        
#         max_len = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 dp[i][j] = dp[i][j-1] + nums[j]
                
#                 if dp[i][j]*2 == j-i+1:
#                     max_len = max(max_len, j-i+1)
#         return max_len

# method 2
# time complexity -- O(N)
# space complexity -- O(N)
# Runtime: 972 ms, faster than 83.01% of Python3 online submissions for Contiguous Array.
# Memory Usage: 18.1 MB, less than 16.67% of Python3 online submissions for Contiguous Array.
# use the brilliant idea: 
# construct a global varibale sum
# if nums[i] == 1, sum += 1; if nums[i] == 0, sum-=1
# if sum == 0, means in a subarray has equal number of 1 and 0
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sub_sum = 0
        record_dict = {0:-1}
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                sub_sum -= 1
            else:
                sub_sum += 1
            if sub_sum in record_dict:
                max_len = max(max_len, i-record_dict[sub_sum])
            else:
                record_dict[sub_sum] = i
        return max_len

