"""
695. Max Area of Island
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""

# Runtime: 148 ms, faster than 58.15% of Python3 online submissions for Max Area of Island.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Max Area of Island.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        bfs = []
        max_area = 0
        visited = set([])
        for i in range(n_row):
            for j in range(n_col):
                if (i, j) in visited:
                    continue
                    
                visited.add((i, j))
                if grid[i][j] == 0:
                    continue
                stack = [[i, j]]
                tmp_area = 1
                while len(stack) != 0:
                    new_pos = stack.pop()
                    for dx, dy in DIRECTIONS:
                        new_row, new_col = new_pos[0] + dx, new_pos[1] + dy
                        if (new_row, new_col) in visited:
                            continue 
                        visited.add((new_row, new_col))
                        if not self.legal_check(new_row, new_col, grid):
                            continue
                        tmp_area += 1
                        stack.append([new_row, new_col])
                max_area = max(tmp_area, max_area)
        return max_area
                        
    def legal_check(self, x, y, grid):
        n_row, n_col = len(grid), len(grid[0])
        return 0<=x<n_row and 0<=y<n_col and grid[x][y] == 1 