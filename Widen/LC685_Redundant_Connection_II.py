"""
685. Redundant Connection II

In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.
"""


# check if a tree is valid
# tutorial: https://www.cnblogs.com/grandyang/p/8445733.html
# Runtime: 64 ms, faster than 59.57% of Python3 online submissions for Redundant Connection II.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Redundant Connection II.
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # if met then gg
        # 30 min didn't get a solution
        # key word: every node has exactly one parent ---> this is a tree
        # so this problem is just to find a valid tree
        # a tree won't be valid under three conditions
        # 1. a node has a link to another node in another subtree
        #       one node will have in_degree of two
        # 2. a node has a link to another node in it's parent
        #       one node will have in_degree of two and there is a loop
        # 3. a node has a link to root node
        #       there will be a loop but all the nodes will have in_degree of one
        
        # actually we just want to return the edge that makes a loop
        # or the second edge that makes a "two-in-degree" node
        # so we mark the second edge, and jump the second edge when doing union find 
        # to form a loop
        parent = collections.defaultdict(int)
        first, second = None, None
        for i in range(len(edges)):
            node1, node2 = edges[i]
            if parent[node2] != 0:
                first = (parent[node2], node2)
                second = (node1, node2)
                edges[i][1] = 0
                continue
            parent[node2] = node1
            
        graph = [i for i in range(len(edges)+1)]
        for i in range(len(edges)):
            if edges[i][1] == 0:
                continue
            node1, node2 = edges[i]
            father1 = self.find(node1, graph)
            father2 = self.find(node2, graph)
            if father1 == father2:
                if first != None:
                    return first
                return (node1, node2)
            graph[father2] = father1
        return second
    
    def find(self, node, graph):
        while node != graph[node]:
            node = graph[node]
        return node
    
        
        
        
            
        
                