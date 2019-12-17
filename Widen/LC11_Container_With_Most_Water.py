"""
11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


# two pointers
# time complexity -- O(N)
# Runtime: 136 ms, faster than 76.05% of Python3 online submissions for Container With Most Water.
# Memory Usage: 14.6 MB, less than 11.58% of Python3 online submissions for Container With Most Water.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        left, right = 0, len(height)-1
        res = -1
        while left < right:
            left_h, right_h = height[left], height[right]
            curr_vol = min(left_h, right_h) * (right-left)
            res = max(res, curr_vol)
            if left_h < right_h:
                left += 1
            else:
                right -= 1
                
        return res