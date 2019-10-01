"""
LC304 -- Range Sum Query 2D - Immutable
time complexity -- O(1)
space complexity -- O(N^2)
Runtime: 132 ms, faster than 50.45% of Python3 online submissions for Range Sum Query 2D - Immutable.
Memory Usage: 16.9 MB, less than 16.67% of Python3 online submissions for Range Sum Query 2D - Immutable.
relatively easy a problem, but be sure to take care of corner case that 
the matrix has only one value
the trick here is to padding zeros around self.dp in advance
"""
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        if n == 0:
            self.dp = 0
        else:
            m = len(matrix[0])
            self.dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
            for i in range(1, n+1):
                for j in range(1, m+1):
                    self.dp[i][j] = -self.dp[i-1][j-1] + self.dp[i-1][j] + self.dp[i][j-1] + matrix[i-1][j-1]
                    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] + self.dp[row1][col1] - self.dp[row1][col2+1] - self.dp[row2+1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)