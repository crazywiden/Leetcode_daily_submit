"""
1153. String Transforms Into Another String
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

 

Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
"""

# so annoying..
# there are three kinds of graph type in this graph
# 1. cycle -- to break a cycle, we must have at least one additional space outside
# 2. self-cycle, we don't do anything, but self-cyle still take on space
# 3. non-cycle, we can conversion anything in non-cycle without outer-space
# Runtime: 24 ms, faster than 85.40% of Python3 online submissions for String Transforms Into Another String.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for String Transforms Into Another String.
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        relation = {}
        self.visited = {}
        for i in range(len(str1)):
            if str1[i] not in relation:
                relation[str1[i]] = str2[i]
            elif str2[i] != relation[str1[i]]:
                return False
        tot_size = 0
        for key in relation:
            if key in self.visited:
                continue
            cycle_size = self.dfs(relation, key, 0)
            tot_size += cycle_size
            if tot_size >= 26:
                return False
        return True
    
    def dfs(self, relation, key, cnt):
        if key in self.visited:
            return cnt - self.visited[key]
        self.visited[key] = cnt
        
        if key not in relation:
            return 0
        if key == relation[key]:
            self.visited[key] = 1
            return 1
        
        return self.dfs(relation, relation[key], cnt+1)


# another brilliant idea!
# Runtime: 20 ms, faster than 96.58% of Python3 online submissions for String Transforms Into Another String.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for String Transforms Into Another String.
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        
        graph = {}
        for i in range(len(str1)):
            if str1[i] not in graph:
                graph[str1[i]] = str2[i]
            elif str2[i] != graph[str1[i]]:
                return False
        return len(set(str2)) < 26
                