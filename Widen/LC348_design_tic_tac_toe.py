"""
LC348 -- Design Tic-Tac-Toe
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
"""

# pretty straight forward implementation... very unefficient though
# Runtime: 692 ms, faster than 5.10% of Python3 online submissions for Design Tic-Tac-Toe.
# Memory Usage: 16.4 MB, less than 16.67% of Python3 online submissions for Design Tic-Tac-Toe.

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.thres = n
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.moves = {1:0, 2:0}
        
        
    def check(self, row, col, player):
        cnt = 0
        # check row
        for i in range(self.thres):
            if self.grid[row][i] == player:
                cnt += 1
            else:
                cnt = 0
            if cnt >= self.thres:
                return player
        cnt = 0
        # check col
        for i in range(self.thres):
            if self.grid[i][col] == player:
                cnt += 1
            else:
                cnt = 0
            if cnt >= self.thres:
                return player
        # check diagnal
        cnt = 0
        for i in range(self.thres):
            if self.grid[i][i] == player:
                cnt += 1
            else:
                cnt = 0
            if cnt >= self.thres:
                return player
        cnt = 0
        for i in range(self.thres):
            if self.grid[i][self.thres-1-i] == player:
                cnt += 1
            else:
                cnt = 0
            if cnt >= self.thres:
                return player
        return 0
            
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.grid[row][col] = player
        self.moves[player] += 1
        if self.moves[1] >= self.thres:
            return self.check(row, col, player)
        if self.moves[2] >= self.thres:
            return self.check(row, col, player)
        return 0
        

# spacial information is not necessary 
# if a player wins, he or she must occupy all grid in that row/col/diagnal
# only number is needed
# Runtime: 100 ms, faster than 87.60% of Python3 online submissions for Design Tic-Tac-Toe.
# Memory Usage: 16.3 MB, less than 16.67% of Python3 online submissions for Design Tic-Tac-Toe.
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.row_num = {i:{1:0, 2:0} for i in range(n)}
        self.col_num = {i:{1:0, 2:0} for i in range(n)}
        self.right_diag_num = {1:0, 2:0}
        self.left_diag_num = {1:0, 2:0}
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.row_num[row][player] += 1
        if self.row_num[row][player] == self.n:
            return player
        
        self.col_num[col][player] += 1
        if self.col_num[col][player] == self.n:
            return player
        
        if row == col:
            self.right_diag_num[player] += 1
            if self.right_diag_num[player] == self.n:
                return player
        if self.n - 1 - row == col:
            self.left_diag_num[player] += 1
            if self.left_diag_num[player] == self.n:
                return player
        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)




