"""
85. Maximal Rectangle
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

# great dp explaination
# tutorial: https://leetcode.com/articles/maximal-rectangle/
# I am so south
# time complexity -- O(MN)
# Runtime: 220 ms, faster than 50.68% of Python3 online submissions for Maximal Rectangle.
# Memory Usage: 14 MB, less than 31.25% of Python3 online submissions for Maximal Rectangle.
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        res = 0
        n_row, n_col = len(matrix), len(matrix[0])
        height = [0 for _ in range(n_col)]
        left_idx = [-1 for _ in range(n_col)]
        right_idx = [n_col for _ in range(n_col)]
        for i in range(n_row):
            left_most_idx, right_most_idx = 0, n_col
            
            # update height
            for j in range(n_col):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
                
            # update left most index
            for j in range(n_col):
                if matrix[i][j] == "1":
                    left_idx[j] = max(left_most_idx, left_idx[j])
                else:
                    left_most_idx = j + 1
                    left_idx[j] = 0
                
            # update the right most index
            for j in range(n_col-1, -1, -1):
                if matrix[i][j] == "1":
                    right_idx[j] = min(right_most_idx, right_idx[j])
                else:
                    right_most_idx = j
                    right_idx[j] = n_col 
            # update result
            for j in range(n_col):
                res = max(res, height[j] * (right_idx[j]-left_idx[j]))
        return res
            
                    