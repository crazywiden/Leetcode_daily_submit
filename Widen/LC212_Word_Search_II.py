"""
LC212 word search II
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""

# application of Trie 

# Runtime: 368 ms, faster than 57.90% of Python3 online submissions for Word Search II.
# Memory Usage: 31 MB, less than 91.67% of Python3 online submissions for Word Search II.
DIRECTIONS = [[0, 1], [0, -1], [-1, 0], [1, 0]]
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.word = ""
        self.children = {}
        
        
class TrieTree:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for l in word:
            if l not in node.children:
                node.children[l] = TrieNode()
            node = node.children[l]
        node.is_word = True
        node.word = word 
        
    def find(self, word):
        node = self.root
        for l in word:
            if l not in node.children:
                return False
            node = node.children[l]
        return node.is_word
    
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        Trie = TrieTree()
        for word in words:
            Trie.insert(word)
            
        res = set([])

        n_row, n_col = len(board), len(board[0])
        for i in range(n_row):
            for j in range(n_col):
                visited = set([(i, j)])
                l = board[i][j]
                self.search(board, i, j, visited, Trie.root.children.get(l), res)
        return res
    
    def search(self, board, row, col, visited, node, res):
        if node == None:
            return 
        
        if node.is_word:
            res.add(node.word)
            
        n_row, n_col = len(board), len(board[0])
        for dx, dy in DIRECTIONS:
            new_row = row + dx
            new_col = col + dy
            if new_row < 0 or new_row >= n_row or new_col < 0 or new_col >= n_col:
                continue
            if (new_row, new_col) in visited:
                continue
            visited.add((new_row, new_col))
            l = board[new_row][new_col]
            self.search(board, new_row, new_col, visited, node.children.get(l), res)
            visited.remove((new_row, new_col))
            