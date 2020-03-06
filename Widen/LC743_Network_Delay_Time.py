"""
743. Network Delay Time
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
"""

# dijsktra algorithm to find minimum path from source to each node
# return the max value of each node
# time complexity -- O(V^2)
# each time need to tranverse all node to find the minimum node
# Runtime: 480 ms, faster than 86.90% of Python3 online submissions for Network Delay Time.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Network Delay Time
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        if len(times) < N-1:
            return -1
        graph = collections.defaultdict(dict)
        for node1, node2, val in times:
            graph[node1][node2] = val
        
        dist = [float("inf") for _ in range(N+1)]
        dist[K] = 0
        visited = set([])
        while len(visited) < N:
            node = self.find_min_dist_node(dist, visited)
            for child in graph[node]:
                dist[child] = min(dist[child], graph[node][child] + dist[node])
            visited.add(node)
        max_dist = max(dist[1:])
        if max_dist == float("inf"):
            return -1
        return max_dist
    
    def find_min_dist_node(self, dist, visited):
        min_dist, min_dist_node = float("inf"), -1
        for i in range(1, len(dist)):
            if i in visited:
                continue
            if dist[i] < min_dist:
                min_dist = dist[i]
                min_dist_node = i
        return min_dist_node
    
    
# better dijsktra
# use heap to maintain heap to find the minimum node each time
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        if len(times) < N-1:
            return -1
        graph = collections.defaultdict(dict)
        for node1, node2, val in times:
            graph[node1][node2] = val 
            
        dist = {i:float("inf") for i in range(1, N+1)}
        dist[K] = 0
        visited = set()
        heap = [(0, K)]
        while heap:
            val, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            for child in graph[node]:
                if graph[node][child] + val < dist[child]:
                    dist[child] = graph[node][child] + val
                    heapq.heappush(heap, (dist[child], child))
                    
        max_time = max(dist.values())
        if max_time == float("inf"):
            return -1
        return max_time
    
        