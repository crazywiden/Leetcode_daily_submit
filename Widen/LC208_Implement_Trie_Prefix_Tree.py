"""
LC208 implement trie
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""
# Runtime: 180 ms, faster than 63.77% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 30.1 MB, less than 18.52% of Python3 online submissions for Implement Trie (Prefix Tree).
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root 
        for l in word:
            if l not in node.children:
                node.children[l] = TrieNode()
            node = node.children[l]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for l in word:
            if l not in node.children:
                return False 
            node = node.children[l]
        return node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for l in prefix:
            if l not in node.children:
                return False 
            node = node.children[l]
        return True