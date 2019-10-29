
"""
LC694 -- number of distinct islands
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""

# bfs 
# Runtime: 252 ms, faster than 67.69% of Python3 online submissions for Number of Distinct Islands.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Number of Distinct Islands.
import heapq
class Solution:
    def numDistinctIslands(self, grid) -> int:
        if len(grid) == 0:
            return 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        cnt = 0
        islands = []
        visited = set()
        n_row = len(grid)
        n_col = len(grid[0])
        for i in range(n_row):
            for j in range(n_col):
                if (i, j) in visited:
                    continue
                if grid[i][j] == 0:
                    continue
                # use bfs to find all the island
                single_island = set()
                queue = []
                heapq.heappush(queue, (i, j))
                while queue:
                    x, y = heapq.heappop(queue)
                    for direction in directions:
                        new_x = x + direction[0]
                        new_y = y + direction[1]
                        if (new_x, new_y) in visited:
                            continue
                        if new_x >=0 and new_x < n_row and new_y >= 0 and new_y < n_col:
                            visited.add((new_x, new_y))
                            if grid[new_x][new_y] == 1:
                                shift = (new_x - i, new_y - j)
                                single_island.add(shift)
                                heapq.heappush(queue, (new_x, new_y))
                if single_island not in islands:
                    cnt += 1
                    islands.append(single_island)
        return cnt





                            
                    
