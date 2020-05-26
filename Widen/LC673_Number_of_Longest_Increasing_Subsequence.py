"""
673. Number of Longest Increasing Subsequence
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
"""

# dp
# time complexity -- O(N^2)
# Runtime: 796 ms, faster than 76.00% of Python3 online submissions for Number of Longest Increasing Subsequence.
# Memory Usage: 13.9 MB, less than 9.09% of Python3 online submissions for Number of Longest Increasing Subsequence.
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        curr_num = 1
        N = len(nums)
        dp = [1 for _ in range(N)]
        len_num = [1 for _ in range(N)]
        for i in range(N):
            base = nums[i]
            base_num = 1
            for j in range(i-1, -1, -1):
                if nums[j] >= nums[i]:
                    continue
                curr_len = dp[j] + 1
                if curr_len > dp[i]:
                    len_num[i] = len_num[j]
                    dp[i] = curr_len
                elif curr_len == dp[i]:
                    len_num[i] += len_num[j]

        max_len = max(dp)
        res = 0
        for i in range(N):
            if dp[i] == max_len:
                res += len_num[i]
        return res
    
        