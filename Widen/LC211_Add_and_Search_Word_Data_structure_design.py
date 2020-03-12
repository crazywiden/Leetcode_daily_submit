"""
211. Add and Search Word - Data structure design
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""
# Trie
# Runtime: 336 ms, faster than 59.71% of Python3 online submissions for Add and Search Word - Data structure design.
# Memory Usage: 27.3 MB, less than 17.39% of Python3 online submissions for Add and Search Word - Data structure design.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        head = self.root 
        for c in word:
            if c not in head.children:
                head.children[c] = TrieNode()
            head = head.children[c]
        head.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        head = self.root
        return self.dfs(head, word)
    
    def dfs(self, root, word):
        if len(word) == 0:
            return root.is_word
        
        if word[0] == ".":
            for key in root.children:
                if self.dfs(root.children[key], word[1:]):
                    return True
            return False
        if word[0] in root.children:
            return self.dfs(root.children[word[0]], word[1:])
        return False
        
        
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)