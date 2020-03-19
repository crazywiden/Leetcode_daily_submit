"""
996. Number of Squareful Arrays
Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

 

Example 1:

Input: [1,17,8]
Output: 2
Explanation: 
[1,8,17] and [17,8,1] are the valid permutations.
Example 2:

Input: [2,2,2]
Output: 1
"""

# dfs 
# most difficult part is to associate this problem with graph
# Runtime: 24 ms, faster than 97.78% of Python3 online submissions for Number of Squareful Arrays.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Number of Squareful Arrays.
import math
class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        graph = collections.defaultdict(set)
        n = len(A)
        for i in range(n-1):
            is_met = False
            for j in range(n):
                if j in graph[i]:
                    is_met = True
                    continue
                tmp = A[j] + A[i]
                if self.check_perfect(tmp):
                    is_met = True
                    graph[j].add(i)
                    graph[i].add(j)
            if not is_met:
                return 0
        
        if n-1 not in graph:
            return 0
        
        res = 0
        val_set = set([])
        for i in range(n):
            tmp = [-1 for _ in range(n)]
            if A[i] in val_set:
                continue
            tmp[0] = i
            val_set.add(A[i])
            cnt = self.dfs(0, tmp, graph, A, set([i]))
            res += cnt
        return res
        
    def dfs(self, idx, tmp, graph, A, visited):
        if idx == len(tmp)-1:
            return 1
        val_set = set([])
        res = 0
        for nei in graph[tmp[idx]]:
            if A[nei] in val_set:
                continue
            if nei in visited:
                continue
            tmp[idx+1] = nei
            val_set.add(A[nei])
            visited.add(nei)
            cnt = self.dfs(idx+1, tmp, graph, A, visited)
            visited.remove(nei)
            res += cnt
        return res                
        
        
    def check_perfect(self, num):
        root = math.sqrt(num)
        return int(root+0.5)**2 == num