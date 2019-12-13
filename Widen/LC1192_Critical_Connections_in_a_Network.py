"""
1192. Critical Connections in a Network
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.
"""


# reference: https://blog.csdn.net/lawfile/article/details/101124841
# reference: https://www.cnblogs.com/nullzx/p/7968110.html

# Runtime: 2580 ms, faster than 44.87% of Python3 online submissions for Critical Connections in a Network.
# Memory Usage: 84.9 MB, less than 100.00% of Python3 online submissions for Critical Connections in a Network.
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        self.graph = defaultdict(list)
        self.low = [i for i in range(n+1)]
        self.dfn = [i for i in range(n+1)]
        self.visited = [False for _ in range(n+1)]
        self.parent = [-1 for _ in range(n+1)]
        self.time_stamp = 0
        self.res = []
        
        for edge in connections:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        
        for i in range(n):
            if not self.visited[i]:
                self.tarjan(i)
        return self.res
    
    def tarjan(self, u):
        self.visited[u] = True
        self.time_stamp += 1
        self.dfn[u] = self.time_stamp
        self.low[u] = self.time_stamp
        for node in self.graph[u]:
            if not self.visited[node]:
                self.parent[node] = u
                self.tarjan(node)
                self.low[u] = min(self.low[u], self.low[node])
                if self.low[node] > self.dfn[u]:
                    self.res.append([u,  node])
                    
            else:
                if node != self.parent[u]:
                    self.low[u] = min(self.low[u], self.dfn[node])
                
                
        
        
        
                