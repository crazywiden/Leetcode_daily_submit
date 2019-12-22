"""
79. Word Search
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

# two tricks used:
# dfs + backtracking
# how to analyze time complexity of backtracking and dfs?
# Runtime: 368 ms, faster than 60.34% of Python3 online submissions for Word Search.
# Memory Usage: 14.1 MB, less than 91.49% of Python3 online submissions for Word Search.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.board = board
        self.n_row = len(board)
        self.n_col = len(board[0])
        
        all_loc = []
        for i in range(self.n_row):
            for j in range(self.n_col):
                if board[i][j] == word[0]:
                    all_loc.append((i, j))
                    
        if len(all_loc) == 0:
            return False
        
        for loc in all_loc:
            visited = set([loc])
            if self.dfs(loc, word[1:], visited):
                return True
        return False
    
    def dfs(self, init_loc, word, visited):
        if len(word) == 0:
            return True
        for d in self.DIRECTIONS:
            x, y = init_loc[0] + d[0], init_loc[1] + d[1]
            if x < 0 or y < 0 or x >= self.n_row or y >= self.n_col:
                continue
            if self.board[x][y] != word[0]:
                continue
            
            new_loc = (x, y)
            if new_loc in visited:
                continue
            visited.add(new_loc)
            if self.dfs(new_loc, word[1:], visited):
                return True
            visited.remove(new_loc)
        return False
                
        
             
            
        