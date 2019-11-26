"""
74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


# be careful about when length of an array is 2
# if len(arr) == 2, use left, right = 0, len(arr)
# Runtime: 72 ms, faster than 83.13% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.8 MB, less than 5.88% of Python3 online submissions for Search a 2D Matrix.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target
        
        left, right = 0, len(matrix)
        # first find the largest number less than target
        while left < right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid
        right = max(right-1, 0)
        if len(matrix[right]) == 1:
            return matrix[right][0] == target
        start, end = 0, len(matrix[right])
        while start < end:
            mid = (start+end) // 2
            if matrix[right][mid] == target:
                return True
            if matrix[right][mid] < target:
                start = mid + 1
            elif matrix[right][mid] > target:
                end = mid
        return False
        
                
                