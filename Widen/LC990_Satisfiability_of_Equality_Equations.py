"""
990. Satisfiability of Equality Equations
Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

 

Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
Example 2:

Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
Example 3:

Input: ["a==b","b==c","a==c"]
Output: true
Example 4:

Input: ["a==b","b!=c","c==a"]
Output: false
Example 5:

Input: ["c==c","b==d","x!=z"]
Output: true
"""

# union find 
# but failed at the first...
# tutorial: https://leetcode.com/articles/satisfiability-of-equality-equations/
# Runtime: 40 ms, faster than 91.64% of Python3 online submissions for Satisfiability of Equality Equations.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Satisfiability of Equality Equations.
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        self.graph = {}
        for eq in equations:
            sign = eq[1:-1]
            if sign == "!=":
                continue
            left_char, right_char = eq[0], eq[-1]
            if left_char not in self.graph:
                self.graph[left_char] = left_char
            if right_char not in self.graph:
                self.graph[right_char] = right_char
            left_father = self.find(left_char)
            right_father = self.find(right_char)
            if left_father != right_father:
                self.graph[left_father] = right_father
        
        for eq in equations:
            sign = eq[1:-1]
            if sign == "==":
                continue
            left_char, right_char = eq[0], eq[-1]
            if left_char == right_char:
                return False
            if left_char not in self.graph or right_char not in self.graph:
                continue
            left_father = self.find(left_char)
            right_father = self.find(right_char)
            if left_father == right_father:
                return False
        return True
    
    def find(self, node):
        tmp = node
        while tmp != self.graph[tmp]:
            tmp = self.graph[tmp]
        father = tmp
        while self.graph[node] != father:
            tmp = self.graph[node]
            self.graph[node] = father
            node = tmp
        return father
    
            