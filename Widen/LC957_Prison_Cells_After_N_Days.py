"""
957. Prison Cells After N Days
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

 

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
"""

# time complexity -- O(N)
# just need to found the status of cells will form a cycle 
# and use hash_map to save the status
# Runtime: 28 ms, faster than 98.84% of Python3 online submissions for Prison Cells After N Days.
# Memory Usage: 13.6 MB, less than 9.09% of Python3 online submissions for Prison Cells After N Days.
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        n = len(cells)
        res = [0 for _ in range(n)]
        state_to_idx = {}
        idx_to_state = {}
        for cnt in range(N):
            for i in range(1, n-1):
                if cells[i-1] == 1 and cells[i+1] == 1:
                    res[i] = 1
                elif cells[i-1] == 0 and cells[i+1] == 0:
                    res[i] = 1
                else:
                    res[i] = 0
            state = "".join([str(i) for i in res])
            if state in state_to_idx:
                start_cnt = state_to_idx[state]
                left_cnt = (N-start_cnt) % cnt
                # print(start_cnt, cnt, left_cnt)
                if left_cnt == 0:
                    return [int(i) for i in idx_to_state[cnt-1]]
                return [int(i) for i in idx_to_state[left_cnt-1]]
            else:
                state_to_idx[state] = cnt
                idx_to_state[cnt] = state
            cells = res.copy()
        return res
    
            