"""
LC505 the maze II
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
"""


# dijkstra
# Runtime: 304 ms, faster than 98.25% of Python3 online submissions for The Maze II.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for The Maze II.
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        dist_mat = [[float('inf')] * len(maze[0]) for _ in range(len(maze))]
        dist_mat[start[0]][start[1]] = 0
        self.dijkstra(maze, start, destination, dist_mat)
        return dist_mat[destination[0]][destination[1]] if dist_mat[destination[0]][destination[1]] != float('inf') else -1
    
    def dijkstra(self, maze, start, destination, dist_mat):
        pq = []
        heapq.heappush(pq, (0, start[0], start[1]))
        while pq:
            dist, i, j = heapq.heappop(pq)
            for d_x, d_y in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_i, new_j, count = i, j, 0
                while 0<=new_i+d_x<len(maze) and 0<=new_j+d_y<len(maze[0]) and maze[new_i+d_x][new_j+d_y] != 1:
                    count += 1
                    new_i += d_x
                    new_j += d_y
                new_dist = dist + count
                if dist_mat[new_i][new_j] > new_dist:
                    dist_mat[new_i][new_j] = new_dist
                    if new_i == destination[0] and new_j == destination[1]:
                        return dist_mat[new_i][new_j]
                    if dist_mat[destination[0]][destination[1]] <= new_dist:
                        continue
                    heapq.heappush(pq, (new_dist, new_i, new_j))