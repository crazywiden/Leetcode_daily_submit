"""
LC1066 Campus Bike II
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.
"""



# a much better solution that mine
# Hungarian method
# time complexity -- 0(n^3)
# amazing!!
# reference: https://leetcode.com/problems/campus-bikes-ii/discuss/305218/DFS-%2B-Pruning-And-DP-Solution
from scipy.optimize import linear_sum_assignment
import numpy as np
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n_worker = len(workers)
        n_bikes = len(bikes)
        dist = [[0 for _ in range(n_bikes)] for _ in range(n_worker)]
        for i in range(n_worker):
            for j in range(n_bikes):
                dist[i][j] = self.cal_dist(workers[i], bikes[j])
        # apply Hungarian Algorithm
        row_idx, col_idx = linear_sum_assignment(dist)
        dist = np.asarray(dist)
        return dist[row_idx, col_idx].sum()
    
    def cal_dist(self, loc1, loc2):
        return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])



# method -- dfs
# TLE
# n -- number of workers /  m -- number of bikes
# time complexity -- O(m!/(m-n)!)
# when size < 10, O(n!) can be accepted
# when size < 15, O(2^n) can be accepted
class Solution:
    def assignBikes(self, workers, bikes) -> int:
        n_worker = len(workers)
        n_bike = len(bikes)
        dist = [[0 for _ in range(n_bike)] for _ in range(n_worker)]
        MAX_INT = 10000000
        for i in range(n_worker):
            for j in range(n_bike):
                dist[i][j] = self.cal_dist(workers[i], bikes[j])
                
        def dfs(dist_mat, start):
            if len(dist_mat) == 0:
                return 0
            if len(dist_mat) == 1:
                return dist_mat[0][start]
            
            visited[start] = 1
            base = dist_mat[0][start]
            min_dist = MAX_INT
            for i in range(n_bike):
                if not visited[i]:
                    visited[i] = 1
                    min_dist = min(min_dist, dfs(dist_mat[1:], i))
                    visited[i] = 0
            return base + min_dist
        
        ans = MAX_INT
        for i in range(n_bike):
            visited = [0 for _ in range(n_bike)]
            ans = min(ans, dfs(dist, i))
        
        return ans
        
    def cal_dist(self, loc1, loc2):
        return abs(loc1[0]-loc2[0]) + abs(loc1[1] - loc2[1])
    


