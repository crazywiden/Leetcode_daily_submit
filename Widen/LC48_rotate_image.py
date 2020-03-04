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
        # outer = int(n/2)
        outer = n // 2 # don't use int(), it's very slowt
        boundary = n - 1
        for i in range(outer):
            inner = n - i*2
            for j in range(i, i+inner-1):
                matrix[j][boundary-i], matrix[boundary-i][boundary-j], matrix[boundary-j][i], matrix[i][j] = matrix[i][j], matrix[j][boundary-i], matrix[boundary-i][boundary-j], matrix[boundary-j][i]

# Runtime: 32 ms, faster than 73.99% of Python3 online submissions for Rotate Image.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Rotate Image.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_edge = len(matrix)
        if n_edge == 0:
            return 
        row = 0
        row_thres = n_edge - row - 1
        while row < row_thres:
            for i in range(row, row_thres):
                x1, y1 = row, i
                x2, y2 = i, row_thres
                x3, y3 = row_thres, n_edge-i-1
                x4, y4 = n_edge-i-1, row
                
                tmp1 = matrix[x1][y1]
                matrix[x1][y1] = matrix[x4][y4]
                tmp2 = matrix[x2][y2]
                matrix[x2][y2] = tmp1
                tmp3 = matrix[x3][y3]
                matrix[x3][y3] = tmp2
                matrix[x4][y4] = tmp3
                
            row += 1
            row_thres = n_edge - row - 1
        
                