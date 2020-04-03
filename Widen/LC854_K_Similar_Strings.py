"""
854. K-Similar Strings
Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:

Input: A = "ab", B = "ba"
Output: 1
Example 2:

Input: A = "abc", B = "bca"
Output: 2
Example 3:

Input: A = "abac", B = "baca"
Output: 2
Example 4:

Input: A = "aabc", B = "abca"
Output: 2
Note:

1 <= A.length == B.length <= 20
A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}
"""


# bfs
# don't think of creating a graph for character exchange... just doesn't work
# tutorial: https://medium.com/@jolyon129/854-k-similar-strings-7b68772217d0
# Runtime: 148 ms, faster than 78.24% of Python3 online submissions for K-Similar Strings.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for K-Similar Strings.
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        new_A, new_B = "", ""
        for i in range(len(A)):
            if A[i] == B[i]:
                continue
            new_A += A[i]
            new_B += B[i]
        A, B = new_A, new_B
        n = len(A)
        if n == 0:
            return 0
        visited = set([])
        deque = [[A, -1, 0]]
        res = n+1
        while deque:
            node, pos, step = deque.pop(0)
            if node == B:
                return step
            for i in range(pos+1, n):
                if node[i] != B[i]: # we have find the first 
                    break
            node_list = list(node)
            for j in range(i+1, n):
                if B[i] == node[j]:
                    node_list[i], node_list[j] = node_list[j], node_list[i]
                    new_str = "".join(node_list)
                    if new_str not in visited:
                        visited.add(new_str)
                        deque.append([new_str, i, step+1])
                    node_list[i], node_list[j] = node_list[j], node_list[i]


# dfs version
# Runtime: 156 ms, faster than 75.31% of Python3 online submissions for K-Similar Strings.
# Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for K-Similar Strings.
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        new_A, new_B = "", ""
        for i in range(len(A)):
            if A[i] == B[i]:
                continue
            new_A += A[i]
            new_B += B[i]
        self.memo = {}
        res = self.dfs(new_A, new_B, -1, 0)  # use backtracking
        return res
     
    def dfs(self, A, B, pos, cnt):
        if A in self.memo:
            return self.memo[A]
        if A == B:
            return 0
        
        res = float("inf")
        A_list = list(A)
        for i in range(pos+1, len(A)):
            if A[i] != B[i]:
                break
        for j in range(i+1, len(A)):
            if A[j] == B[i] and A[j] != B[j]:
                A_list[j], A_list[i] = A_list[i], A_list[j]
                new_A = "".join(A_list)
                tmp = self.dfs(new_A, B, i, cnt) + 1
                A_list[j], A_list[i] = A_list[i], A_list[j]
                res = min(res, tmp)
        self.memo[A] = res
        return res




    
        
