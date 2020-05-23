# 764. Largest Plus Sign
# In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

# An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

# Runtime: 3484 ms, faster than 31.20% of Python3 online submissions for Largest Plus Sign.
# Memory Usage: 50.1 MB, less than 16.67% of Python3 online submissions for Largest Plus Sign.
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        grid = [[1 for _ in range(N)] for _ in range(N)]
        for x, y in mines:
            grid[x][y] = 0
        search = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]
        # search[i][0] -- how many 1's on the left
        # search[i][1] -- how many 1's on the right
        # search[i][2] -- how many 1's from above
        # search[i][3] -- how many 1's from below
        
        # initialize
        for i in range(N):
            if grid[i][0] == 1:
                search[i][0][0] = 1
            if grid[i][-1] == 1:
                search[i][-1][1] = 1
            if grid[0][i] == 1:
                search[0][i][2] = 1
            if grid[-1][i] == 1:
                search[-1][i][3] = 1
        res = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    res = 1
                    break
                    
        # update left and above
        for i in range(1, N-1):
            for j in range(1, N-1):
                if grid[i][j] == 0:
                    continue
                search[i][j][0] = search[i][j-1][0] + 1
                search[i][j][2] = search[i-1][j][2] + 1
        
        # update right and below
        for i in range(N-2, 0, -1):
            for j in range(N-2, 0, -1):
                if grid[i][j] == 0:
                    continue
                search[i][j][1] = search[i][j+1][1] + 1
                search[i][j][3] = search[i+1][j][3] + 1

        for i in range(N):
            for j in range(N):
                curr_res = min(search[i][j])
                if curr_res == 0:
                    continue
                res = max(res, curr_res)
        
        return res
    
                
        