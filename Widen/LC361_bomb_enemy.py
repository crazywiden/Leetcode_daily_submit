"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), 
return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until 
it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
"""
# reference: https://blog.csdn.net/qq508618087/article/details/51705806
# actually my initial thoughts are right
# don't hesitate to implement your solution!!!
# implement a solution is better than no solution!!
# time complexity -- O(M*N)
# space complexity -- O(M*N)
# Runtime: 348 ms, faster than 72.65% of Python3 online submissions for Bomb Enemy.
# Memory Usage: 14.8 MB, less than 30.00% of Python3 online submissions for Bomb Enemy.

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        n = len(grid)
        m = len(grid[0])
        
        cnt = 0
        row_cnt = 0
        col_cnt = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if i == 0 or grid[i-1][j] == "W":
                    col_cnt[j] = 0
                    for row in range(i, n):
                        if grid[row][j] == "W":
                            break
                        if grid[row][j] == "E":
                            col_cnt[j] += 1
                if j == 0 or grid[i][j-1] == "W":
                    row_cnt = 0
                    for col in range(j, m):
                        if grid[i][col] == "W":
                            break
                        if grid[i][col] == "E":
                            row_cnt += 1
                if grid[i][j] == "0":
                    cnt = max(cnt, row_cnt + col_cnt[j])
        return cnt
                        
        
            
                
        
