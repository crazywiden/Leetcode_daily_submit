"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.
"""

# Runtime: 80 ms, faster than 59.60% of Python3 online submissions for Longest Continuous Increasing Subsequence.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Longest Continuous Increasing Subsequence.
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        tmp, res = 1, 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                tmp += 1
            else:
                res = max(res, tmp)
                tmp = 1
                
        return max(res, tmp)