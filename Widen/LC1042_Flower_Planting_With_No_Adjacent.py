"""
1042. Flower Planting With No Adjacent
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

 

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
"""

# pay attention to details!!
# Runtime: 600 ms, faster than 14.83% of Python3 online submissions for Flower Planting With No Adjacent.
# Memory Usage: 27.5 MB, less than 100.00% of Python3 online submissions for Flower Planting With No Adjacent.
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        self.res = [0 for _ in range(N+1)]
        for node1, node2 in paths:
            graph[node1].add(node2)
            graph[node2].add(node1)
        
        for i in range(N):
            for color in range(1, 5):
                self.dfs(i, graph)
        for i in range(1, N+1):
            if self.res[i] == 0:
                self.res[i] = 1
        return self.res[1:]
    
    def dfs(self, node, graph):
        if self.res[node] != 0:
            return 
        
        all_color = set(range(1, 5))
        for nei in graph[node]:
            if self.res[nei] != 0 and self.res[nei] in all_color:
                all_color.remove(self.res[nei])
        all_color = list(all_color)
        self.res[node] = all_color[0]
        for nei in graph[node]:
            self.dfs(nei, graph)
            
                
        
        
        
        