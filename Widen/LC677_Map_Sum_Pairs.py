"""
677. Map Sum Pairs
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""

# Trie
# time complexity -- O(N)
# Runtime: 20 ms, faster than 99.05% of Python3 online submissions for Map Sum Pairs.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Map Sum Pairs.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.val = 0 
        
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        head = self.root
        for c in key:
            if c not in head.children:
                head.children[c] = TrieNode()
            head = head.children[c]
        head.is_word = True
        head.val = val 

    def sum(self, prefix: str) -> int:
        head = self.root
        for c in prefix:
            if c in head.children:
                head = head.children[c]
            else:
                return 0
        return self.dfs(head)

    def dfs(self, head):
        res = 0
        if head.is_word:
            res += head.val 
        for c in head.children:
            res += self.dfs(head.children[c])
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)