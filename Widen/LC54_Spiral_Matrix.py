"""
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


# Runtime: 28 ms, faster than 64.68% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Spiral Matrix.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        if len(matrix[0]) == 0:
            return []
        n_row, n_col = len(matrix), len(matrix[0])
        
        row, col = 0, -1
        res = []
        visited = set([])
        DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        is_done = False
        while not is_done:
            is_done = True
            dx, dy = DIRECTIONS.pop(0)
            DIRECTIONS.append([dx, dy])
            while (row+dx, col+dy) not in visited:
                if row+dx >= n_row or row+dx < 0 or col+dy >= n_col or col+dy < 0:
                    break
                if (row+dx, col+dy) in visited:
                    break
                is_done = False
                row, col = row + dx, col + dy
                visited.add((row, col))
                res.append(matrix[row][col])
        return res
    
# application of yield
# very convenient!!
# Runtime: 28 ms, faster than 64.68% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Spiral Matrix.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def index_order(r1, r2, c1, c2):
            for c in range(c1, c2+1):
                yield r1, c
            for r in range(r1+1, r2+1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2-1, c1-1, -1):
                    yield r2, c

                for r in range(r2-1, r1, -1):
                    yield r, c1
                
        if len(matrix) == 0:
            return []
        
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        res = []
        while r1<=r2 and c1<=c2:
            for row, col in index_order(r1, r2, c1, c2):
                res.append(matrix[row][col])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return res

    
            