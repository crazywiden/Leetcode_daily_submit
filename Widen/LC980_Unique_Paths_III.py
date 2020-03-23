"""
980. Unique Paths III
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20
"""

# i love dfs and backtracking
# Runtime: 52 ms, faster than 85.34% of Python3 online submissions for Unique Paths III.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Unique Paths III.
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # self.memo = {}
        n_row, n_col = len(grid), len(grid[0])
        tot_num = 0
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 0:
                    tot_num += 1
                if grid[i][j] == 1:
                    start_x, start_y = i, j
        
        res = self.dfs(grid, start_x, start_y, set([]), 1, tot_num)
        
        return res
    
    def dfs(self, grid, x, y, visited, cnt, tot_num):
        if grid[x][y] == -1:
            return 0
        if grid[x][y] == 2:
            if len(visited) != tot_num+1:
                return 0
            return 1
        
        n_row, n_col = len(grid), len(grid[0])
        tot_method = 0
        for dx, dy in self.DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= n_row or new_y < 0 or new_y >= n_col:
                continue
            if (new_x, new_y) in visited:
                continue
            if grid[new_x][new_y] == -1:
                continue
            if grid[new_x][new_y] == 1:
                continue
            visited.add((new_x, new_y))
            tot_method += self.dfs(grid, new_x, new_y, visited, cnt, tot_num)
            visited.remove((new_x, new_y))
        return cnt * tot_method
        # return self.memo[(x, y)]
    
        
        