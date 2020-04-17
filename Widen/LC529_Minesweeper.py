"""
529. Minesweeper
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
"""

# bfs
# time complexity -- O(nm)
# space complexity -- O(1)
# Runtime: 196 ms, faster than 64.87% of Python3 online submissions for Minesweeper.
# Memory Usage: 13.9 MB, less than 60.00% of Python3 online submissions for Minesweeper.
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n_row, n_col = len(board), len(board[0])
        x, y = click
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        
        visited = set([])
        digits = set([str(i) for i in range(1, 9)])
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, -1], [-1, 1], [1, 1], [-1, -1]]
        deque = [[x, y]]
        while deque:
            x, y = deque.pop(0)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if board[x][y] != "E":
                continue
            board[x][y] = "B"
            num_mine = 0
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_x >= n_row or new_y < 0 or new_y >= n_col:
                    continue
                if board[new_x][new_y] in ["X", "M"]:
                    num_mine += 1
            if num_mine > 0:
                board[x][y] = str(num_mine)
                continue
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_x >= n_row or new_y < 0 or new_y >= n_col:
                    continue
                if (new_x, new_y) in visited:
                    continue
                    
                if board[new_x][new_y] == "E":
                    deque.append([new_x, new_y])
        return board
    
            
        