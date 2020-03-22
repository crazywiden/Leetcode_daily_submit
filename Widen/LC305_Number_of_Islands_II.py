
"""
305. Number of Islands II
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
"""

# union find 
# Runtime: 556 ms, faster than 60.78% of Python3 online submissions for Number of Islands II.
# Memory Usage: 17.5 MB, less than 25.00% of Python3 online submissions for Number of Islands II.
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        k = len(positions)
        res = [0 for _ in range(k)]
        cnt = 0
        self.union_find_set = {}
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i, (x, y) in enumerate(positions):
            if (x, y) in self.union_find_set:
                res[i] = cnt
                continue
                
            self.union_find_set[(x, y)] = (x, y)
            cnt += 1
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_x >= m or new_y < 0 or new_y > n:
                    continue
                if (new_x, new_y) not in self.union_find_set:
                    continue
                father1 = self.find((new_x, new_y))
                if father1 != (x, y):
                    self.union_find_set[father1] = (x, y)
                    cnt -= 1
            res[i] = cnt
        return res
    
    def find(self, loc):
        tmp = loc
        while self.union_find_set[tmp] != tmp:
            tmp = self.union_find_set[tmp]
        father = tmp
        while self.union_find_set[loc] != father:
            tmp = self.union_find_set[loc]
            self.union_find_set[loc] = father
            loc = tmp
        return father
    
        