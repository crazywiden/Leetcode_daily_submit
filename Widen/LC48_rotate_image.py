"""
LC 525 -- Contiguous Array
Description:
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""
# time complexity -- O(N^2)
# space complexity -- O(1)
# Runtime: 48 ms, faster than 12.00% of Python3 online submissions for Rotate Image.
# Memory Usage: 14.1 MB, less than 6.25% of Python3 online submissions for Rotate Image.
# use the brilliant idea: 
# nothing special, just tedious mathematics

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        outer = int(n/2)
        boundary = n - 1
        for i in range(outer):
            inner = n - i*2
            for j in range(i, i+inner-1):
                matrix[j][boundary-i], matrix[boundary-i][boundary-j], matrix[boundary-j][i], matrix[i][j] = matrix[i][j], matrix[j][boundary-i], matrix[boundary-i][boundary-j], matrix[boundary-j][i]
                