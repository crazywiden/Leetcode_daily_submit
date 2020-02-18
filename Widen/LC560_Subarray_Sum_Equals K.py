"""
LC560 subarray sum equals
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""


# Runtime: 96 ms, faster than 99.87% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 16.8 MB, less than 20.00% of Python3 online submissions for Subarray Sum Equals K.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # O(n^2) solution -- TLE
#         n = len(nums)
#         prefix_sum = [0 for _ in range(n+1)]
#         for i in range(1, n+1):
#             prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
            
#         cnt = 0
#         for i in range(n+1):
#             for j in range(i+1, n+1):
#                 if prefix_sum[j] - prefix_sum[i] == k:
#                     cnt += 1
#         return cnt
    
        # O(n) solution
        n = len(nums)
        sum_dict = collections.defaultdict(int)
        sum_dict[0] = 1
        prefix_sum = 0
        res = 0
        for i in range(n):
            prefix_sum += nums[i]
            res += sum_dict[prefix_sum-k]
            sum_dict[prefix_sum] += 1
        return res
        