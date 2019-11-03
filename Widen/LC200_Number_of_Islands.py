"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""



# dfs
# why my efficiency is always so low!!!
# Runtime: 172 ms, faster than 35.15% of Python3 online submissions for Number of Islands.
# Memory Usage: 19.3 MB, less than 5.13% of Python3 online submissions for Number of Islands.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        all_island = []
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        def dfs(x, y):
            if (x, y) in visited:
                return 
            if x < 0 or x >= n or y < 0 or y >= m:
                return 
            if grid[x][y] == "0":
                return 
            visited.add((x, y))
            for chg in directions:
                dfs(x+chg[0], y+chg[1])
                    
                
        cnt = 0
        for i in range(n):
            for j in range(m):
                if (i, j) in visited:
                    continue
                if grid[i][j] == "0":
                    continue
                dfs(i, j)
                cnt += 1
        return cnt


