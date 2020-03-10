"""
1197. Minimum Knight Moves
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
"""

# traditional bfs
# very very slow...
# Runtime: 6704 ms, faster than 8.95% of Python3 online submissions for Minimum Knight Moves.
# Memory Usage: 58.4 MB, less than 100.00% of Python3 online submissions for Minimum Knight Moves.
class Solution:
    def minKnightMoves(self, row: int, col: int) -> int:
        if row == 0 and col == 0:
            return 0
        DIRECTIONS = [[-1, -2], [-2, -1], [1, -2], [2, -1],
                [-2, 1], [-1, 2], [2, 1], [1, 2]]
        res = 1
        deque = [[0, 0]]
        visited = set([])
        visited.add((0, 0))
        tmp = []
        while deque:
            x, y = deque.pop(0)
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy 
                if (new_x, new_y) in visited:
                    continue 
                if new_x == row and new_y == col:
                    return res 
                tmp.append([new_x, new_y])
                visited.add((new_x, new_y))
            if len(deque) == 0:
                deque = tmp.copy()
                res += 1
                tmp = []
                
        return -1 
    
    