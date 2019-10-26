"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""



# bfs using deque
# pretty much new method for me
# Runtime: 300 ms, faster than 75.37% of Python3 online submissions for Walls and Gates.
# Memory Usage: 16.7 MB, less than 60.00% of Python3 online submissions for Walls and Gates.
import collections
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []
        n_row = len(rooms)
        n_col = len(rooms[0])
        bfs = collections.deque()
        for i in range(n_row):
            for j in range(n_col):
                if rooms[i][j] == 0:
                    bfs.append((i, j))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while bfs:
            x, y = bfs.popleft()
            dist = rooms[x][y] + 1
            for direction in directions:
                new_x, new_y = x + direction[0], y + direction[1]
                if new_x >=0 and new_x < n_row and new_y >= 0 and new_y < n_col and rooms[new_x][new_y] == 2147483647:
                    rooms[new_x][new_y] = dist
                    bfs.append((new_x, new_y))
        
        