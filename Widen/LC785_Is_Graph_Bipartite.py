"""
785. Is Graph Bipartite?

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
"""


# should be coloring method
# should have check the solution earlier
# wasted a lot of time
# tutorial: https://www.cnblogs.com/grandyang/p/8519566.html
# time complexity: O(E+V) space complexity:O(E)

# bfs
# the following solution is wrong because the graph might be not connected
# e.g. [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # bfs
        n = len(graph)
        deque = [0]
        colors = [0 for _ in range(n)]
        colors[0] = 1
        while deque:
            node = deque.pop(0)
            for nei in graph[node]:
                if colors[nei] == colors[node]:
                    return False
                if colors[nei] == 0:
                    colors[nei] = -1*colors[node]
                    deque.append(nei)
        return True


# modify -- add a loop to traverse all the node
# Runtime: 180 ms, faster than 91.09% of Python3 online submissions for Is Graph Bipartite?.
# Memory Usage: 13.1 MB, less than 90.91% of Python3 online submissions for Is Graph Bipartite?.
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0 for _ in range(n)]
        for i in range(n):
            if colors[i] != 0:
                continue
            colors[i] = 1
            deque = [i]
            while deque:
                node = deque.pop(0)
                for nei in graph[node]:
                    if colors[node] == colors[nei]:
                        return False
                    if colors[nei] == 0:
                        deque.append(nei)
                        colors[nei] = -1*colors[node]
        return True
    

# real dfs
# Runtime: 180 ms, faster than 91.09% of Python3 online submissions for Is Graph Bipartite?.
# Memory Usage: 13 MB, less than 90.91% of Python3 online submissions for Is Graph Bipartite?.
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0 for _ in range(n)]
        for i in range(n):
            if colors[i] == 0 and (not self.valid(graph, 1, i, colors)):
                return False
        return True
    
    def valid(self, graph, color, curr, colors):
        if colors[curr] != 0:
            return colors[curr] == color
        colors[curr] = color
        for node in graph[curr]:
            if not self.valid(graph, -1*color, node, colors):
                return False
        return True
    
# TLE
# greedy, not dfs at all
# time complexity -- O(2^N)
# this solution should be correct
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.memo = {}
        return self.dfs(graph, 0, set([]))
    
    def dfs(self, graph, start, in_set):
        if (start, tuple(in_set)) in self.memo:
            return self.memo[(start,tuple(in_set))]
        if start >= len(graph):
            return True
        if start in in_set:
            for node in graph[start]:
                if node in in_set:
                    self.memo[(start, tuple(in_set))] = False
                    return False
            self.memo[(start, tuple(in_set))] = self.dfs(graph, start+1, in_set)
            return self.memo[(start, tuple(in_set))]
        
        if start not in in_set:
            # we have two choices here
            # 1. add the neighborhood into in_set
            # 2. add start into in_set
            # we should first check the first condition
            # if one node in the neighborhood in already in the inset
            # then we have to choose 1
            for node in graph[start]:
                if node in in_set:
                    in_set.update(graph[start])
                    self.memo[(start, tuple(in_set))] = self.dfs(graph, start+1, in_set)
                    return self.memo[(start, tuple(in_set))]
            
            # try no.2
            in_set.add(start)
            start_in = self.dfs(graph, start+1, in_set)
            in_set.remove(start)
            
            in_set.update(graph[start])
            start_not_in = self.dfs(graph, start+1, in_set)
            
            if start_in or start_not_in:
                self.memo[(start, tuple(in_set))] = True
                return True
            self.memo[(start, tuple(in_set))] = False
            return False
        
        