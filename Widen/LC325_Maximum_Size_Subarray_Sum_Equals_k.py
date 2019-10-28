"""
LC325 325. Maximum Size Subarray Sum Equals k
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
"""


# dp, similar to one problem to find maximum length of sum zero
# Runtime: 132 ms, faster than 81.91% of Python3 online submissions for Maximum Size Subarray Sum Equals k.
# Memory Usage: 17 MB, less than 20.00% of Python3 online submissions for Maximum Size Subarray Sum Equals k.
class Solution:
    def maxSubArrayLen(self, nums, k) -> int:
        if len(nums) == 0:
            return 0
        sub_sum = 0
        sum_dict = {}
        cnt = 0
        for i in range(len(nums)):
            sub_sum += nums[i]
            if sub_sum not in sum_dict:
                sum_dict[sub_sum] = i
            if sub_sum == k:
                cnt = max(cnt, i+1)
            if (sub_sum - k) in sum_dict:
                cnt = max(cnt, i-sum_dict[sub_sum-k])
        return cnt

# little trick: init dic with key 0 and value -1
# then don't need to check when sub_sum == k
# Runtime: 124 ms, faster than 98.02% of Python3 online submissions for Maximum Size Subarray Sum Equals k.
# Memory Usage: 16.8 MB, less than 20.00% of Python3 online submissions for Maximum Size Subarray Sum Equals k.
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
         
        dic = {0:-1}
        summ = 0
        maxlen = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ - k in dic and i-dic[summ-k] > maxlen:
                maxlen = i-dic[summ-k]
            if summ not in dic:
                dic[summ] = i
        return maxlen