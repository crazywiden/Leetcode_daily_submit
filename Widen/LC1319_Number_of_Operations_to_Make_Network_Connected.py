"""
1319. Number of Operations to Make Network Connected
There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1. 

 
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
"""

# union find to calculate the number of connected component
# actually don't need to calculate redundant cable number
# if the number of connections is less than n-1, return -1
# slower than dfs or bfs because we have *find* method
# Runtime: 600 ms, faster than 30.80% of Python3 online submissions for Number of Operations to Make Network Connected.
# Memory Usage: 32.9 MB, less than 100.00% of Python3 online submissions for Number of Operations to Make Network Connected.
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # res == number of connected component - 1
        redundant_cable = 0
        self.parent = [i for i in range(n)]
        for node1, node2 in connections:
            father1 = self.find(node1)
            father2 = self.find(node2)
            if father1 == father2 and (node1 != father1 or node2 != father2):
                redundant_cable += 1
            if father1 != father2:
                self.parent[father2] = father1
        
        connected_component = collections.defaultdict(list)
        for i in range(n):
            father = self.find(i)
            connected_component[father].append(i)
        num_connected = len(connected_component)
        if num_connected - 1 > redundant_cable:
            return -1
        return num_connected - 1
    
    def find(self, node):
        tmp = node
        while tmp != self.parent[tmp]:
            tmp = self.parent[tmp]
        father = tmp
        
        # path compression
        while self.parent[node] != father:
            tmp = self.parent[node]
            self.parent[node] = father
            node = tmp
        return father

# dfs to find the number of connected component
# Runtime: 520 ms, faster than 90.31% of Python3 online submissions for Number of Operations to Make Network Connected.
# Memory Usage: 43.7 MB, less than 100.00% of Python3 online submissions for Number of Operations to Make Network Connected.
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        # build graph
        graph = collections.defaultdict(list)
        for node1, node2 in connections:
            graph[node1].append(node2)
            graph[node2].append(node1)
        # find 
        num, self.visited = 0, set([])
        for i in range(n):
            if i not in self.visited:
                self.dfs(i, graph)
                num += 1
        return num - 1
    
    def dfs(self, node, graph):
        if node in self.visited:
            return 
        self.visited.add(node)
        for child in graph[node]:
            self.dfs(child, graph)
        

# bfs to find the number of connected component
# Runtime: 484 ms, faster than 99.64% of Python3 online submissions for Number of Operations to Make Network Connected.
# Memory Usage: 33.1 MB, less than 100.00% of Python3 online submissions for Number of Operations to Make Network Connected.
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        # build graph
        graph = collections.defaultdict(list)
        for node1, node2 in connections:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        num, visited = 0, set([])
        for i in range(n):
            if i in visited:
                continue
            visited.add(i)
            num += 1
            deque = [i]
            while deque:
                node = deque.pop(0)
                for child in graph[node]:
                    if child in visited:
                        continue
                    visited.add(child)
                    deque.append(child)
        return num - 1




        