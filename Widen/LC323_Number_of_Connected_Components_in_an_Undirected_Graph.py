"""
LC323. Number of Connected Components in an Undirected Graph
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""




# union find set
# turns out not very efficient??
# Runtime: 132 ms, faster than 29.80% of Python3 online submissions for Number of Connected Components in an Undirected Graph.
# Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions for Number of Connected Components in an Undirected Graph.
import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        self.father = collections.defaultdict(int)
        for i in range(len(edges)):
            self.father[edges[i][0]] = edges[i][0]
            self.father[edges[i][1]] = edges[i][1]
        self.cnt = n
        for i in range(len(edges)):
            self.union(edges[i][0], edges[i][1])
        return self.cnt
            

    def find(self, node):
        path = []
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]
        for point in path:
            self.father[point] = node
        return node
            

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        
        if parent_a < parent_b:
            self.father[parent_b] = parent_a
            self.cnt -= 1
        elif parent_a > parent_b:
            self.father[parent_a] = parent_b
            self.cnt -= 1
        


# best solution are all dfs...

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    dfs(next_node)
        graph = collections.defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = set()
        ans = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                ans += 1
        return ans  