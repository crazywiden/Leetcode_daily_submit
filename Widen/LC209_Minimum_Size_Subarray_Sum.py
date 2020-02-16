"""
209. Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

"""

# two pointer
# if the array also contains negative integer
# use prefix sum + monotonic deque
# time complexity --O(N)
# Runtime: 76 ms, faster than 70.79% of Python3 online submissions for Minimum Size Subarray Sum.
# Memory Usage: 15.2 MB, less than 7.69% of Python3 online submissions for Minimum Size Subarray Sum.
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        res = n+1
        left, right = 0, 0
        tmp = 0
        for left in range(n):
            while right < n and tmp < s:
                tmp += nums[right]
                right += 1 
            if tmp < s:
                break
            res = min(res, right-left)
            tmp -= nums[left]
            
        if res == n+1:
            return 0
        return res

# sorted
# time complexity -- O(nlogn)


