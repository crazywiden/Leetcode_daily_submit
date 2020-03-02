"""
LC399 -- Evaluate Division
This question was asked in ThoughtSpot on campus interview
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
"""


# best part of this problem is to transform this problem to a graph problem
# use Union Find -- also create a dictionary to perform union and find, which is genius
# reference: https://zxi.mytechroad.com/blog/graph/leetcode-399-evaluate-division/
# Runtime: 20 ms, faster than 98.04% of Python3 online submissions for Evaluate Division.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Evaluate Division.
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def find(node):
            if node != UnionFindDict[node][0]:
                parent, val = find(UnionFindDict[node][0])
                UnionFindDict[node] = (parent, val * UnionFindDict[node][1])
            return UnionFindDict[node]
        
        def divide(node1, node2):
            parent1, val1 = find(node1)
            parent2, val2 = find(node2)
            if parent1 != parent2:
                return -1
            return val1/val2
            
        # each key is a node
        # each value is a tuple
        #   value[0] is parent of this node
        #   value[1] is the distance from child to parent
        UnionFindDict = {}
        for (child, parent), val in zip(equations, values):
            if (child not in UnionFindDict) and (parent not in UnionFindDict):
                UnionFindDict[child] = (parent, val)
                UnionFindDict[parent] = (parent, 1.0)
            elif child not in UnionFindDict:
                UnionFindDict[child] = (parent, val)
            elif parent not in UnionFindDict:
                UnionFindDict[parent] = (child, 1.0/val)
            else: # perform union find
                x_parent, x_val = find(child)
                y_parent, y_val = find(parent)
                UnionFindDict[y_parent] = (x_parent, x_val/(y_val * val))
        res = [divide(x, y) if x in UnionFindDict and y in UnionFindDict else -1 for x, y in queries]
        return res


# dfs solution
# Runtime: 24 ms, faster than 89.16% of Python3 online submissions for Evaluate Division.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Evaluate Division.
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for i in range(len(equations)):
            node1, node2 = equations[i]
            graph[node1][node2] = values[i]
            graph[node2][node1] = 1.0 / values[i]
        n = len(queries)
        res = [0 for _ in range(n)]
        for i in range(n):
            node1, node2 = queries[i]
            res[i] = self.dfs(graph, node1, node2, set([node1]), 1)
        return res 
    
    def dfs(self, graph, node1, node2, visited, res):
        if node1 not in graph:
            return -1 
        if node2 in graph[node1]:
            return res * graph[node1][node2]
        flag = False
        for node in graph[node1]:
            if node in visited:
                continue
            visited.add(node)
            tmp = self.dfs(graph, node, node2, visited, res*graph[node1][node])
            if tmp != -1:
                flag = True
                res = tmp
        if not flag:
            return -1
        return res
            