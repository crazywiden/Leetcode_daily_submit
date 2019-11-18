"""
133. Clone Graph
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
"""

# bfs
# Runtime: 32 ms, faster than 98.88% of Python3 online submissions for Clone Graph.
# Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Clone Graph.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        root = node
        if not node:
            return root
        all_node = self.get_all_node(node)
        
        # copy all node
        mapping = {}
        for node in all_node:
            mapping[node] = Node(node.val, [])

        # copy edges
        for node in all_node:
            new_node = mapping[node]
            for child in node.neighbors:
                new_child = mapping[child]
                new_node.neighbors.append(new_child)
        
        return mapping[root]
    def get_all_node(self, root):
        q = deque([root])
        visited = set([root])
        while q:
            new_node = q.popleft()
            for child in new_node.neighbors:
                if child not in visited:
                    visited.add(child)
                    q.append(child)
        return visited