"""
128. Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

# soooo smart!!
# tutorial: https://leetcode.com/articles/longest-consecutive-sequence/
# Runtime: 52 ms, faster than 85.96% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 15.1 MB, less than 7.41% of Python3 online submissions for Longest Consecutive Sequence.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                curr_num = num
                curr_len = 1
                
                while curr_num + 1 in nums:
                    curr_num += 1
                    curr_len += 1
                res = max(res, curr_len)
        return res
    