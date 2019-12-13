"""
289. Game of Life
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
"""


# easy
# Runtime: 28 ms, faster than 94.90% of Python3 online submissions for Game of Life.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Game of Life.
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_neighbor = {}
        n_row = len(board)
        if n_row == 0:
            return []
        directions = [
            [-1, 0], [1, 0], [0, 1], [0, -1],
            [-1, -1], [-1, 1], [1, -1], [1, 1]
        ]
        n_col = len(board[0])
        for i in range(n_row):
            for j in range(n_col):
                n = 0
                for d in directions:
                    x, y = i + d[0], j + d[1]
                    if x < 0 or x >= n_row or y < 0 or y >= n_col:
                        continue
                    if board[x][y] == 1:
                        n += 1
                num_neighbor[(i,j)] = n
                
        for key in num_neighbor.keys():
            x, y = key[0], key[1]
            n = num_neighbor[key]
            if board[x][y]==1 and n<2:
                board[x][y] = 0
            elif board[x][y]==1 and n>3:
                board[x][y] = 0
            elif board[x][y]==0 and n==3:
                board[x][y] = 1
        
        