"""
LC 787 Cheapest Flights within k stops
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
"""

# first intuition -- dfs with memory
# Runtime: 256 ms, faster than 11.95% of Python3 online submissions for Cheapest Flights Within K Stops.
# Memory Usage: 15.5 MB, less than 52.63% of Python3 online submissions for Cheapest Flights Within K Stops.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        MAX = 1000000000
        graph = [[0 for _ in range(n)] for _ in range(n)]
        for trip in flights:
            graph[trip[0]][trip[1]] = trip[2]
        memo = {}  # memo[(i, k)] -- cheapest cost from city i to dst within k stops
        def dfs(start, k):
            if start == dst:
                memo[(start, 0)] = graph[start][dst]
                return graph[start][dst]
            if k == 0:
                return MAX
            
            price = MAX
            for i in range(n):
                if graph[start][i] != 0:
                    if (i, k-1) in memo:
                        price = min(price, graph[start][i] + memo[(i, k-1)])
                    else:
                        price = min(price, graph[start][i] + dfs(i, k-1))
            memo[(start, k)] = price
            return price
        
        res = dfs(src, K+1)
        if res == MAX:
            return -1
        else: 
            return res
    
# method 2 -- Dijkstra's algorithm
# Runtime: 108 ms, faster than 63.24% of Python3 online submissions for Cheapest Flights Within K Stops.
# Memory Usage: 19.7 MB, less than 26.32% of Python3 online submissions for Cheapest Flights Within K Stops.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    	import collections
    	import heapq
        graph = collections.defaultdict(dict)
        for a, b, price in flights:
            graph[a][b] = price
        
        pq = [(0, K+1, src)]
        # heapq will sort by the first element in the tuple
        # https://stackoverflow.com/questions/3954530/how-to-make-heapq-evaluate-the-heap-off-of-a-specific-attribute
        while pq:
            price, k, pos = heapq.heappop(pq)
            if pos == dst:
                return price
            if k > 0:
                newpos = graph[pos]
                for p in newpos:
                    heapq.heappush(pq, (price+newpos[p], k-1, p))
        return -1




# method 3 -- bfs, not very good, but worth learn
# Runtime: 124 ms, faster than 37.62% of Python3 online submissions for Cheapest Flights Within K Stops.
# Memory Usage: 14.6 MB, less than 52.63% of Python3 online submissions for Cheapest Flights Within K Stops.

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(dict)
        for u, v, e in flights:
            graph[u][v] = e
        ans = float('inf')
        que = collections.deque()
        que.append((src, 0))
        step = 0
        while que:
            size = len(que)
            for i in range(size):
                cur, cost = que.popleft()
                if cur == dst:
                    ans = min(ans, cost)
                for v, w in graph[cur].items():
                    if cost + w > ans:
                        continue
                    que.append((v, cost + w))
            if step > K: break
            step += 1
        return -1 if ans == float('inf') else ans
