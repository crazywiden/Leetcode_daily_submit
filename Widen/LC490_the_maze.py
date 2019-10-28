"""
LC490 The maze
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
"""


# dfs
# Runtime: 336 ms, faster than 56.66% of Python3 online submissions for The Maze.
# Memory Usage: 15.8 MB, less than 7.69% of Python3 online submissions for The Maze.
class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        # using dfs
        if len(maze) == 0:
            return False
        visited = set()
        n_row = len(maze)
        n_col = len(maze[0])
        
        def dfs(start_loc):
            x, y = start_loc
            visited.add((x, y))
            reachable = []
            for i in range(y+1, n_col):
                if (x, i) in visited:
                    continue
                if maze[x][i] == 1:
                    break
                if (i == n_col - 1) or maze[x][i+1] == 1:
                    reachable.append([x, i])
            for i in range(y-1, -1, -1):
                if (x, i) in visited:
                    continue
                if maze[x][i] == 1:
                    break
                if (i == 0) or maze[x][i-1] == 1:
                    reachable.append([x, i])
                
            for j in range(x+1, n_row):
                if (j, y) in visited:
                    continue
                if maze[j][y] == 1:
                    break
                if (j == n_row - 1) or maze[j+1][y] == 1:
                    reachable.append([j, y])
            for j in range(x-1, -1, -1):
                if (j, y) in visited:
                    continue
                if maze[j][y] == 1:
                    break
                if (j == 0) or maze[j-1][y] == 1:
                    reachable.append([j, y])
            if len(reachable) == 0:
                return False
            if destination in reachable:
                return True
            for loc in reachable:
                if dfs(loc):
                    return True
            return False
        
        return dfs(start)
        




