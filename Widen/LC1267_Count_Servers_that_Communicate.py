"""
1267. Count Servers that Communicate
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.
"""
# another simple idea
# time complexity -- O(MN)
# space complexity -- O(M+N)
# Runtime: 504 ms, faster than 87.11% of Python3 online submissions for Count Servers that Communicate.
# Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions for Count Servers that Communicate.
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        row_cnt = [0 for _ in range(n_row)]
        col_cnt = [0 for _ in range(n_col)]
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 1:
                    row_cnt[i] += 1
                    col_cnt[j] += 1
        res = 0
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 0:
                    continue
                if row_cnt[i] == 1 and col_cnt[j] == 1:
                    continue
                res += 1
        return res


# very very very very simple idea
# time complexity -- O(NM)
# space complexity -- O(1)
# tutorial:https://www.acwing.com/solution/LeetCode/content/6493/
# Runtime: 568 ms, faster than 27.59% of Python3 online submissions for Count Servers that Communicate.
# Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Count Servers that Communicate.
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        for i in range(n_row):
            cnt = 0
            for j in range(n_col):
                if grid[i][j] >= 1:
                    cnt += 1
            if cnt <= 1:
                continue
            
            for j in range(n_col):
                if grid[i][j] == 1:
                    grid[i][j] = 2
        for j in range(n_col):
            cnt = 0
            for i in range(n_row):
                if grid[i][j] >= 1:
                    cnt += 1
            if cnt <= 1:
                continue
            
            for i in range(n_row):
                if grid[i][j] == 1:
                    grid[i][j] = 2
        res = 0
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 2:
                    res += 1
        return res


# bfs
# time complexity -- O(MN*max(M, N))
# turns out i think too complicated...
# maybe I am a little familiar with the common schema
# now it's time to summarize the common schema and think of specific solution for specific problems
# Runtime: 948 ms, faster than 6.86% of Python3 online submissions for Count Servers that Communicate.
# Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Count Servers that Communicate.
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # bfs
        n_row, n_col = len(grid), len(grid[0])
        visited = set([])
        res = 0
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 0:
                    continue
                if (i, j) in visited:
                    continue
                cnt = 1
                deque = [(i, j)]
                visited.add((i, j))
                while deque:
                    x, y = deque.pop(0)
                    for new_x in range(n_row):
                        if grid[new_x][y] == 0:
                            continue
                        if (new_x, y) in visited:
                            continue
                        deque.append((new_x, y))
                        cnt += 1
                        visited.add((new_x, y))
                    
                    for new_y in range(n_col):
                        if grid[x][new_y] == 0:
                            continue
                        if (x, new_y) in visited:
                            continue
                        deque.append((x, new_y))
                        cnt += 1
                        visited.add((x, new_y))
                if cnt > 1:
                    res += cnt
        return res
    
        