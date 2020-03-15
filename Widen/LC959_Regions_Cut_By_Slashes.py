"""
959. Regions Cut By Slashes
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

 

Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
"""
# this is a problem to find number of connected components
# either use union find or dfs
# dfs
# very annoying to analyze all possible outcomes
# time complexity -- O(N*M)
# Runtime: 156 ms, faster than 88.22% of Python3 online submissions for Regions Cut By Slashes.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Regions Cut By Slashes.
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        node = {(0, 1):False, (0, -1): False, (1, 0):False, (-1, 0):False}
        self.graph = [[node.copy() for _ in range(n_col)] for _ in range(n_row)]
        self.direct_loc = {(0, 1):(-1, 0), (1, 0):(0, 1), 
                           (-1, 0):(0, -1), (0, -1):(1, 0)}
        num_area = 0
        for i in range(n_row):
            for j in range(n_col):
                for key in self.graph[i][j].keys():
                    if self.graph[i][j][key]:
                        continue 
                    # print(i, j, key)
                    self.dfs(i, j, key, grid)
                    num_area += 1
        return num_area
    
    def dfs(self, x, y, loc, grid):
        n_row, n_col = len(grid), len(grid[0])
        if self.graph[x][y][loc]:
            return 
        
        self.graph[x][y][loc] = True
        if grid[x][y] == "/":
            if loc == (-1, 0):
                self.graph[x][y][(0, 1)] = True
                new_directions = [[-1, 0], [0, -1]]
            elif loc == (0, 1):
                self.graph[x][y][(-1, 0)] = True
                new_directions = [[-1, 0], [0, -1]]
            elif loc == (1, 0):
                self.graph[x][y][(0, -1)] = True
                new_directions = [[1, 0], [0, 1]]
            elif loc == (0, -1):
                self.graph[x][y][(1, 0)] = True
                new_directions = [[1, 0], [0, 1]]
        elif grid[x][y] == "\\":
            if loc == (-1, 0):
                self.graph[x][y][(0, -1)] = True
                new_directions = [[0, -1], [1, 0]]
            elif loc == (0, -1):
                self.graph[x][y][(-1, 0)] = True
                new_directions = [[0, -1], [1, 0]]
            elif loc == (1, 0):
                self.graph[x][y][(0, 1)] = True
                new_directions = [[0, 1], [-1, 0]]
            elif loc == (0, 1):
                self.graph[x][y][(1, 0)] = True
                new_directions = [[0, 1], [-1, 0]]
        elif grid[x][y] == " ":
            for key in self.graph[x][y].keys():
                self.graph[x][y][key] = True
            new_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
        for dx, dy in new_directions:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= n_row or new_y < 0 or new_y >= n_col:
                continue
            new_loc = self.direct_loc[(dx, dy)]
            self.dfs(new_x, new_y, new_loc, grid)
    