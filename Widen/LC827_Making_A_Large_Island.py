"""
827. Making A Large Island
In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
"""

# also can be solved by naive dfs and bfs
# union find
# time complexity -- O(NM)
# space complexity -- O(MN)
# Runtime: 244 ms, faster than 14.73% of Python3 online submissions for Making A Large Island.
# Memory Usage: 14 MB, less than 86.37% of Python3 online submissions for Making A Large Island.
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        n_row, n_col = len(grid), len(grid[0])
        parent = {}
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 0:
                    continue
                parent[(i, j)] = [(i, j), 1]  # [parent_loc, num_group]
                
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 0:
                    continue
                base_father = self.find(parent, (i, j))
                for dx, dy in DIRECTIONS:
                    new_x, new_y = i + dx, j + dy
                    if new_x < 0 or new_x >= n_row or new_y < 0 or new_y >= n_col:
                        continue
                    if grid[new_x][new_y] == 0:
                        continue
                    father = self.find(parent, (new_x, new_y))
                    if base_father != father:
                        parent[father][0] = base_father
                        parent[base_father][1] += parent[father][1]
                        
        res = -1        
        for x in range(n_row):
            for y in range(n_col):
                if grid[x][y] == 1:
                    continue
                tmp_res = self.island_size(grid, parent, x, y, DIRECTIONS)
                res = max(tmp_res, res)
        if res == -1:
            return n_row * n_col
        return res
    
    def find(self, parent, loc):
        x, y = loc
        # print(loc)
        # find parent
        while parent[(x, y)][0] != (x, y):
            x, y = parent[(x, y)][0]
            
        # path compression
        father_x, father_y = x, y
        while parent[loc][0] != (father_x, father_y):
            parent[loc][1] = parent[(father_x, father_y)][1]
            loc = parent[loc][0]
        return (father_x, father_y)
        

    def island_size(self, grid, parent, x, y, DIRECTIONS):
        n_row, n_col = len(grid), len(grid[0])
        res = 1
        neighbor = {}
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= n_row or new_y < 0 or new_y >= n_col:
                continue
            if grid[new_x][new_y] == 0:
                continue
            father_x, father_y = self.find(parent, (new_x, new_y))
            if (father_x, father_y) in neighbor:
                continue
            neighbor[(father_x, father_y)] = parent[(father_x, father_y)][1]
        for key, val in neighbor.items():
            res += val
        return res
            
    
    
        