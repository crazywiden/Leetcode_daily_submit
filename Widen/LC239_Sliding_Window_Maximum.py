"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""


# deque solution in O(N)
# Runtime: 168 ms, faster than 61.20% of Python3 online submissions for Sliding Window Maximum.
# Memory Usage: 19.4 MB, less than 88.46% of Python3 online submissions for Sliding Window Maximum.
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k or k == 0:
            return []
        
        stack = deque([0])
        res = []
        for i in range(1, k):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
        res.append(nums[stack[0]])
        
        for i in range(k, len(nums)):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
            if i - stack[0] >= k:
                stack.popleft()
            res.append(nums[stack[0]])
        return res
        