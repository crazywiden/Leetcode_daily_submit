"""
802. Find Eventual Safe States
In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.
"""

# directionaly graph
# topological sort and in-degree / out-degree
# time complexity -- O(N)
# Runtime: 780 ms, faster than 28.14% of Python3 online submissions for Find Eventual Safe States.
# Memory Usage: 20.2 MB, less than 7.69% of Python3 online submissions for Find Eventual Safe States.
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # similar to topological sort
        # but this time we deal with out-degree
        # every time a node has out-degree of zero
        # we add this node to the result
        n = len(graph)
        out_degree = [0 for _ in range(n)]
        parent = collections.defaultdict(set)
        for father, children in enumerate(graph):
            for child in children:
                parent[child].add(father)
                out_degree[father] += 1
        deque = []
        res = []
        for i in range(n):
            if out_degree[i] == 0:
                deque.append(i)
                res.append(i)
                
        while deque:
            node = deque.pop(0)
            for father in parent[node]:
                out_degree[father] -= 1
                if out_degree[father] == 0:
                    res.append(father)
                    deque.append(father)
        return sorted(res)


# dfs solution
# use status to denote three conditions of a node: unvisited / safe / unsafe
# be careful about the default value of a condition when visited it
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # dfs solution
        n = len(graph)
        res = []
        # 0 -- unvisited
        # 1 -- safe
        # 2 -- unsafe
        status = [0 for _ in range(n)]
        for i in range(n):
            if self.dfs(graph, i, status):
                res.append(i)
        return sorted(res)
    
    def dfs(self, graph, start, status):
        if status[start] != 0:
            return status[start] == 1
        status[start] = 2 # default is unsafe
        for child in graph[start]:
            if not self.dfs(graph, child, status):
                # if this node can reach a loop
                return False
            
        status[start] = 1
        return True





                