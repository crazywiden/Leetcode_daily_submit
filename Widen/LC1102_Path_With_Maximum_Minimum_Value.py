"""
1102. Path With Maximum Minimum Value
Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

 

Example 1:



Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: 
The path with the maximum score is highlighted in yellow. 
Example 2:



Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:
Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3
"""

# greedy again
# no bfs no dfs no dp
# should practice more greedy algorithm
# Runtime: 1304 ms, faster than 61.06% of Python3 online submissions for Path With Maximum Minimum Value.
# Memory Usage: 15.7 MB, less than 100.00% of Python3 online submissions for Path With Maximum Minimum Value.
import heapq
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        # max heap solution
        
        visited = set([(0, 0)])
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n_row, n_col = len(A), len(A[0])
        res = min(A[0][0], A[-1][-1])
        max_heap = [[-A[0][0], (0, 0)]]
        while max_heap:
            val, loc = heapq.heappop(max_heap)
            val = -val
            res = min(res, val)
            x, y = loc
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if new_x<0 or new_x>=n_row or new_y<0 or new_y>=n_col:
                    continue
                if (new_x, new_y) in visited:
                    continue
                if new_x == n_row-1 and new_y == n_col-1:
                    return res
                visited.add((new_x, new_y))
                heapq.heappush(max_heap, [-A[new_x][new_y], (new_x, new_y)])
        return res
    
        
        
# Runtime: 2588 ms, faster than 8.26% of Python3 online submissions for Path With Maximum Minimum Value.
# Memory Usage: 17.5 MB, less than 100.00% of Python3 online submissions for Path With Maximum Minimum Value.
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        n_row, n_col = len(A), len(A[0])
        self.union_find_set = collections.defaultdict()
        all_ele = []
        for i in range(n_row):
            for j in range(n_col):
                all_ele.append([A[i][j], (i, j)])
                self.union_find_set[(i, j)] = (i, j)
        res = min(A[0][0], A[-1][-1])
        all_ele = sorted(all_ele, key=lambda x:x[0])
        visited = set([(0, 0), (n_row-1, n_col-1)])
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while self.find((0, 0)) != self.find((n_row-1, n_col-1)):
            val, loc = all_ele.pop()
            res = min(res, val)
            x, y = loc
            visited.add((x, y))
            base_parent = self.find((x, y))
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if new_x<0 or new_x >= n_row or new_y<0 or new_y>=n_col:
                    continue
                if (new_x, new_y) not in visited:
                    continue
                visited.add((new_x, new_y))
                parent = self.find((new_x, new_y))
                if parent != base_parent:
                    self.union_find_set[parent] = base_parent
        return res
    
    def find(self, loc):
        tmp = loc
        while self.union_find_set[tmp] != tmp:
            tmp = self.union_find_set[tmp]
        father = tmp
        while self.union_find_set[loc] != father:
            tmp = self.union_find_set[loc]
            self.union_find_set[loc] = father
            loc = tmp
        return father


        
                