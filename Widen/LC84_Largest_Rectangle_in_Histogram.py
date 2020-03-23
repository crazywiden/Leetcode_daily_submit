"""
84. Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""
# monotonic stack
# Runtime: 136 ms, faster than 11.37% of Python3 online submissions for Largest Rectangle in Histogram.
# Memory Usage: 15.1 MB, less than 13.64% of Python3 online submissions for Largest Rectangle in Histogram.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic stack
        n = len(heights)
        if n == 0:
            return 0
        res = 0
        left_most_idx = [0 for _ in range(n)]
        right_most_idx = [n for _ in range(n)]
        left_stack = []
        for i in range(n):
            while left_stack and heights[left_stack[-1]] >= heights[i]:
                left_stack.pop()
            if len(left_stack) == 0:
                left_most_idx[i] = - 1
            else:
                left_most_idx[i] = left_stack[-1] 
            left_stack.append(i)
        # print(left_most_idx)
        right_stack = []
        for i in range(n-1, -1, -1):
            while right_stack and heights[right_stack[-1]] >= heights[i]:
                right_stack.pop()
            if len(right_stack) == 0:
                right_most_idx[i] = n
            else:
                right_most_idx[i] = right_stack[-1]
            right_stack.append(i)
        # print(right_most_idx)
        for i in range(n):
            res = max(res, heights[i] * (right_most_idx[i] - left_most_idx[i] - 1))
            
        return res
    
                
            
        