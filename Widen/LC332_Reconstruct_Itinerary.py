"""
332. Reconstruct Itinerary
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

# backtracking
# need to flag the edges in a graph
# time complexity -- O(E^d)
# where E is the number of edges, d is the maximum number of flights from one airport
# Runtime: 96 ms, faster than 29.41% of Python3 online submissions for Reconstruct Itinerary.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Reconstruct Itinerary.
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        graph = collections.defaultdict(list)
        for start, end in tickets:
            graph[start].append([end, False])
        for key in graph.keys():
            graph[key] = sorted(graph[key])
        return self.dfs("JFK", n, ["JFK"], graph)
    
    def dfs(self, start, remain_n, prev_travel, graph):
        if remain_n == 0:
            return prev_travel
        for i in range(len(graph[start])):
            if graph[start][i][1]:
                continue 
            graph[start][i][1] = True
            node = graph[start][i][0]
            nxt_travel = self.dfs(node, remain_n-1, [node], graph)
            graph[start][i][1] = False
            if nxt_travel != None:
                return prev_travel + nxt_travel
        return None
            
        

# Hierholzer's Algorithm
# ???
# 
        