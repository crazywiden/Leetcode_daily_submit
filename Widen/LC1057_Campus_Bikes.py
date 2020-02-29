"""
1057. Campus Bikes

On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.
"""

# greedy method
# time complexity -- O(m*n log (m*n)): used to sort all pairs
# Runtime: 2124 ms, faster than 8.12% of Python3 online submissions for Campus Bikes.
# Memory Usage: 254.8 MB, less than 100.00% of Python3 online submissions for Campus Bikes
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n_worker, n_bike = len(workers), len(bikes)
        pairs = []
        for i in range(n_worker):
            for j in range(n_bike):
                dist = self.cal_dist(workers[i], bikes[j])
                pairs.append([dist, i, j])
        pairs = sorted(pairs, key=lambda x:(x[0], x[1], x[2]))
        
        visited_worker = [False for _ in range(n_worker)]
        visited_bike = [False for _ in range(n_bike)]
        res = [-1 for _ in range(n_worker)]
        for i in range(len(pairs)):
            _, worker_id, bike_id = pairs[i]
            if visited_worker[worker_id] or visited_bike[bike_id]:
                continue 
            res[worker_id] = bike_id
            visited_worker[worker_id] = True
            visited_bike[bike_id] = True
        return res
    def cal_dist(self, worker, bike):
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

# we can speed this up
# two tricks that speed the whole things up:
# 1. transform bikes from list to dictionary, so every time we delete element from bikes, takes O(1)
# 2. only find bike of cloest distance from worker to bikes, avoid O(mnlog mn) sort but with O(mn)
import heapq
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n_worker, n_bike = len(workers), len(bikes)
        bikes = dict(enumerate(bikes))
        heap = []
        for idx, worker in enumerate(workers):
            dist, bike_idx = self.find_cloest(worker, bikes)
            heapq.heappush(heap, (dist, idx, bike_idx))

        visited_bike = set([])
        res = [-1 for _ in range(n_worker)]
        while len(visited_bike) < n_worker:
            dist, worker_id, bike_idx = heapq.heappop(heap)
            # print(dist, worker_id, bike_idx)
            if bike_idx in visited_bike:
                dist, bike_idx = self.find_cloest(workers[worker_id], bikes)
                heapq.heappush(heap, (dist, worker_id, bike_idx))
            else:
                visited_bike.add(bike_idx)
                res[worker_id] = bike_idx
                del bikes[bike_idx]
        return res
    
    def find_cloest(self, worker, bikes):
        min_dist = float("inf")
        min_idx = -1
        for idx, bike in bikes.items():
            dist = self.cal_dist(worker, bike)
            if dist < min_dist:
                min_dist = dist
                min_idx = idx
        return min_dist, min_idx
    
    def cal_dist(self, worker, bike):
        return abs(worker[0] - bike[0]) + abs(bike[1] - worker[1])


                