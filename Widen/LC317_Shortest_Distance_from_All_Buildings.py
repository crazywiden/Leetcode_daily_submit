"""
LC 317 317. Shortest Distance from All Buildings
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
"""


# first hard by myself!!!
# efficiency is very very very low though

# Runtime: 1432 ms, faster than 5.08% of Python online submissions for Shortest Distance from All Buildings.
# Memory Usage: 14.6 MB, less than 50.00% of Python online submissions for Shortest Distance from All Buildings.

# just BFS
import collections
import copy
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # find location of buildings
        N = len(grid)
        M = len(grid[0])
        building_indices = []
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    building_indices.append([i,j])
        distance_mat = []
        for i in range(len(building_indices)):
            distance = self.find_dist_map(grid, building_indices[i])
            distance_mat.append(distance)
        return self.find_min(distance_mat, grid)
        
        
    def find_dist_map(self, new_grid, building_idx):
        # should mark 1/2 as -1 and -2, respectively
        grid = copy.deepcopy(new_grid)
        bfs = collections.deque()
        visited = set()
        
        n_row = len(grid)
        n_col = len(grid[0])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        x, y = building_idx
        grid[x][y] = -1
        bfs.append((x, y))
        visited.add((x, y))
        dist = 0
        while bfs:
            x, y = bfs.popleft()
            if grid[x][y] == -1:
                dist = 1
            else:
                dist = grid[x][y] + 1
            for direction in directions:    
                new_x, new_y = x + direction[0], y + direction[1]
                if (new_x, new_y) in visited:
                	continue
                if new_x >= 0 and new_x < n_row and new_y >= 0 and new_y < n_col:
                    if grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = -1
                    elif grid[new_x][new_y] == 2:
                        grid[new_x][new_y] = -2
                    elif grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = dist
                        bfs.append((new_x, new_y))
                    visited.add((new_x, new_y))
        return grid
                        
    def find_min(self, distance_mat, grid):
        res = 100000
        N = len(distance_mat)
        n_row = len(distance_mat[0])
        n_col = len(distance_mat[0][0])
        for row in range(n_row):
            for col in range(n_col):
                is_reach_all = True
                if grid[row][col] in [1, 2]:
                    continue
                cnt = 0
                for i in range(N):
                    if distance_mat[i][row][col] == 0:
                        is_reach_all = False
                        break
                    cnt += distance_mat[i][row][col]
                if is_reach_all:
                    res = min(res, cnt)
        if res == 100000:
        	return -1
        return res


# a powerful solution also using bfs
# Runtime: 84 ms, faster than 81.91% of Python online submissions for Shortest Distance from All Buildings.
# Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for Shortest Distance from All Buildings.
'''
Use hit to record how many times a 0 grid has been reached and use distSum to record the sum of distance from all 1 grids to this 0 grid. A powerful pruning is that during the BFS we use count1 to count how many 1 grids we reached. If count1 < buildings then we know not all 1 grids are connected are we can return -1 immediately, which greatly improved speed (beat 100% submissions).
'''

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        n, m = len(grid), len(grid[0])
        buildings = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    buildings += 1
        hit = [[0]*m for _ in range(n)]
        disSum = [[0]*m for _ in range(n)]

        def bfs(start_x, start_y):
            visited = [[False]*m for _ in range(n)]
            visited[start_x][start_y] = True
            q = collections.deque([(start_x, start_y, 0)])
            # make sure every building can reach other buildings
            count1 = 1
            while q:
                x, y, dist = q.popleft()
                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0 <= nx < n  and 0 <= ny < m and not visited[nx][ny]:
                        visited[nx][ny] = True
                        if not grid[nx][ny]:
                            q.append((nx, ny, dist + 1))
                            disSum[nx][ny] += dist+1
                            hit[nx][ny] += 1
                        if grid[nx][ny] == 1:
                            count1 += 1
            return count1 == buildings

        for i in range(n):
            for j in range(m):
                # BFS on each building, check if all buildings can be reached as well as updating each 0 with the steps it took to get there.
                if grid[i][j] == 1:
                    if not bfs(i, j):
                        return -1
        min_dist = float('inf')
        for i in range(n):
            for j in range(m):
                if hit[i][j] == buildings:
                    min_dist = min(min_dist, disSum[i][j])
        return -1 if min_dist == float('inf') else min_dist        
            