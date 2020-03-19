"""
1129. Shortest Path with Alternating Colors
Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

 

Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
"""

# bfs
# almost always bfs when dealing with shortest length problem
# this bfs used 2d array to store distance
# brilliant idea
# Runtime: 80 ms, faster than 97.97% of Python3 online submissions for Shortest Path with Alternating Colors.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Shortest Path with Alternating Colors.
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = {0:collections.defaultdict(set), 1:collections.defaultdict(set)}
        res = [[float("inf") for _ in range(n)] for _ in range(2)]
        res[0][0] = 0
        res[1][0] = 0
        
        for node, nxt_node in red_edges:
            graph[0][node].add(nxt_node)
        for node, nxt_node in blue_edges:
            graph[1][node].add(nxt_node)
        
        deque = [(0, 0, 0), (0, 1, 0)]
        
        while deque:
            node, color, step = deque.pop(0)    
            nxt_color = 1 - color
            for nxt_node in graph[nxt_color][node]:
                if res[nxt_color][nxt_node] <= step + 1:
                    continue
                res[nxt_color][nxt_node] = step + 1
                deque.append([nxt_node, nxt_color, step+1])
        
        final_res = [float("inf") for _ in range(n)]
        for i in range(n):
            final_res[i] = min(res[0][i], res[1][i])
            if final_res[i] == float("inf"):
                final_res[i] = -1
        return final_res
        
    
    
    
    
        
    
        
