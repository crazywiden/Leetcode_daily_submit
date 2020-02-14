"""
"""


# actually is a problem to check if there were loops in a graph
# correct solution is to use topological sort
# don't use UNION FIND!

# Runtime: 100 ms, faster than 73.47% of Python3 online submissions for Course Schedule.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Course Schedule.
class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0 for _ in range(n)]
        dependencies = collections.defaultdict(set)
        for i in range(len(prerequisites)):
            child, father = prerequisites[i]
            dependencies[father].add(child)
            in_degree[child] += 1 
            
        root = []
        for i in range(n):
            if in_degree[i] == 0:
                root.append(i)
        if len(root) == 0:
            return False
        # bfs
        while len(root) != 0:
            tmp = root.pop(0)
            for val in dependencies[tmp]:
                in_degree[val] -= 1 
                if in_degree[val] == 0:
                    root.append(val)
                    
        for i in range(n):
            if in_degree[i] != 0:
                return False
        return True 
        