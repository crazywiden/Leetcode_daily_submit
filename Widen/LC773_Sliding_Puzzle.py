"""
773. Sliding Puzzle
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
"""

# bfs
# be extremely careful about the deepcopy of 2d list in python
# Time Complexity: O(R * C * (R * C)!)O(R∗C∗(R∗C)!), where R, CR,C are the number of rows and columns in board. There are O((R * C)!)O((R∗C)!) possible board states.
# Space Complexity: O(R * C * (R * C)!)O(R∗C∗(R∗C)!).

import copy
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        visited = set([])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        n_row, n_col = len(board), len(board[0])
        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == 0:
                    init_x, init_y = i, j
                    break
        init_status = self.get_status(board)
        if init_status == "123450":
            return 0
        visited.add(init_status)
        deque = [[board, init_x, init_y, 0]]
        while deque:
            board, x, y, step = deque.pop(0)
            for dx, dy in DIRECTIONS:
                new_x, new_y = x+dx, y+dy
                if new_x < 0 or new_x >= n_row or new_y < 0 or new_y >= n_col:
                    continue
                new_board = copy.deepcopy(board)
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                new_status = self.get_status(new_board)
                # print(new_status, )
                if new_status in visited:
                    continue
                if new_status == "123450":
                    return step + 1
                deque.append([new_board, new_x, new_y, step+1])
                visited.add(new_status)
        return -1
    
    def get_status(self, board):
        res = ""
        for i in range(len(board)):
            for j in range(len(board[0])):
                res += str(board[i][j])
        return res