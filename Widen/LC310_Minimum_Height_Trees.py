"""
310. Minimum Height Trees
For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
"""
# bfs from leaves node
# a very important question for bfs and dfs
# which node to start?
# definiation of leaves node: degree is 1
# time complexity -- O(N), each node visited only once
# space complexity -- O(N), build graph etc.
# Runtime: 256 ms, faster than 65.59% of Python3 online submissions for Minimum Height Trees.
# Memory Usage: 16.6 MB, less than 75.00% of Python3 online submissions for Minimum Height Trees.
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]
        degrees = [0 for _ in range(n)]
        graph = collections.defaultdict(list)
        for node1, node2 in edges:
            degrees[node1] += 1
            degrees[node2] += 1
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        curr_leaves = []
        visited = set([])
        for i in range(n):
            if degrees[i] == 1:
                curr_leaves.append(i)
        while len(visited) < n-2:
            next_level = []
            for node in curr_leaves:
                visited.add(node)
                for nei in graph[node]:
                    if nei in visited:
                        continue
                    degrees[nei] -= 1
                    if degrees[nei] == 1:
                        next_level.append(nei)
            curr_leaves = next_level.copy()
        return curr_leaves


