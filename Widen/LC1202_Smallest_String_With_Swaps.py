"""
1202. Smallest String With Swaps
"""

# union find solution
# please be sure that union find the most suitable solution for 
# connection, especially non-directional connection
# Runtime: 1476 ms, faster than 5.05% of Python3 online submissions for Smallest String With Swaps.
# Memory Usage: 49.4 MB, less than 100.00% of Python3 online submissions for Smallest String With Swaps.
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        self.parent = [i for i in range(n)]
        for node1, node2 in pairs:
            father1 = self.find(node1)
            father2 = self.find(node2)
            if father1 != father2:
                self.parent[father2] = father1 

        group = collections.defaultdict(str)
        for i in range(n):
            father = self.find(i)
            group[father] += s[i]
        for key in group.keys():
            group[key] = sorted(group[key])
        
        s = list(s)
        for i in range(n):
            group_idx = self.find(i)
            s[i] = group[group_idx][0]
            group[group_idx].pop(0)
        return "".join(s) 
        
    def find(self, node):
        tmp = node
        while self.parent[tmp] != tmp:
            tmp = self.parent[tmp]
        root = tmp
        tmp = node
        while self.parent[tmp] != root:
            father = self.parent[tmp]
            self.parent[tmp] = root
            tmp = father
        return root
    
            
            
            
            
            
            

# TLE
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        self.parent = [i for i in range(n)]
        for node1, node2 in pairs:
            father1 = self.find(node1)
            father2 = self.find(node2)
            if father1 != father2:
                self.parent[father2] = father1 

        group = collections.defaultdict(str)
        for i in range(n):
            father = self.find(i)
            group[father] += s[i]
        for key in group.keys():
            group[key] = sorted(group[key])
        
        s = list(s)
        for i in range(n):
            group_idx = self.find(i)
            s[i] = group[group_idx][0]
            group[group_idx] = group[group_idx][1:]  # very time consuming
        return "".join(s) 
        
    def find(self, node):
        tmp = node
        while self.parent[tmp] != tmp:
            tmp = self.parent[tmp]
        root = tmp
        tmp = node
        while self.parent[tmp] != root:
            father = self.parent[tmp]
            self.parent[tmp] = root
            tmp = father
        return root
    
            
            
            
            
            
            