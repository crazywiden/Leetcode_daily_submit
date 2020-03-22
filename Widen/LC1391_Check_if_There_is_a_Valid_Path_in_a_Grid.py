"""
1391. Check if There is a Valid Path in a Grid

"""

# very tedis problem + a little dfs
# but very similar to the real world problems
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        valid_path_seg = {
            (0, 1): [1, 3, 5],
            (0, -1): [1, 4, 6],
            (1, 0): [2, 5, 6],
            (-1, 0): [2, 3, 4]
        }
        seg_dirs = {
            1: [(0, -1), (0, 1)],
            2: [(1, 0), (-1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(1, 0), (0, 1)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)]
        }
        
        curr_loc = (0, 0)
        visited = set([(0, 0)])
        return self.dfs((0, 0), grid, visited, seg_dirs, valid_path_seg)

    def dfs(self, curr_loc, grid, visited, seg_dirs, valid_path_seg):
        n_row, n_col = len(grid), len(grid[0])
        x, y = curr_loc
        if x == n_row - 1 and y == n_col - 1:
            return True
        
        dirs = seg_dirs[grid[x][y]]
        can_finish = False
        for dx, dy in dirs:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in visited:
                continue
            if new_x < 0 or new_x>=n_row or new_y < 0 or new_y >= n_col:
                continue
            if grid[new_x][new_y] not in valid_path_seg[(dx, dy)]:
                continue
            visited.add((new_x, new_y))
            can_finish = self.dfs((new_x, new_y), grid, visited, seg_dirs, valid_path_seg) or can_finish
        return can_finish
            
        