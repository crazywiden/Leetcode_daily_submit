"""
LC261. Graph Valid Tree
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""


# method 1: BFS
# deque is a good thing
# Runtime: 92 ms, faster than 98.52% of Python3 online submissions for Graph Valid Tree.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Graph Valid Tree.
from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        is_visited = set([0])
        bfs_q = deque([0])
        connection = [set() for _ in range(n)]
        for edge in edges:
            connection[edge[0]].add(edge[1])
            connection[edge[1]].add(edge[0])

        while bfs_q:
            new_node = bfs_q.popleft()
            for node in connection[new_node]:
                if node in is_visited:
                    return False
                bfs_q.append(node)
                is_visited.add(node)
                connection[node].remove(new_node)
        if len(is_visited) != n:
            return False
        return True
                
        

# method 2: union find
# pay attention to loop
# Runtime: 100 ms, faster than 93.32% of Python3 online submissions for Graph Valid Tree.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Graph Valid Tree.

from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.union_set = defaultdict(int)
        self.is_loop = False
        for i in range(n):
            self.union_set[i] = -1
        for edge in edges:
            self.union(edge[0], edge[1])
            if self.is_loop:
                return False
        num_root = 0
        for key, val in self.union_set.items():
            if val < 0:
                num_root += 1
        return num_root == 1
            
            
    def find(self, node):
        # print(node)
        if self.union_set[node] < 0:
            return node
        return self.find(self.union_set[node])
    
    def union(self, node1, node2):
        # print("new")
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        
        if parent1 == parent2 and parent1 != -1:
            self.is_loop = True
            return
        # print(self.union_set)
        if self.union_set[parent1] < self.union_set[parent2]: 
            self.union_set[parent1] += self.union_set[parent2]
            self.union_set[node2] = parent1
            self.union_set[parent2] = parent1
        else:
            self.union_set[parent2] += self.union_set[parent1]
            self.union_set[node1] = parent2
            self.union_set[parent1] = parent2
        # print(self.union_set)
        





