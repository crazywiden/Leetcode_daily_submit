"""
1036. Escape a Large Maze
In a 1 million by 1 million grid, the coordinates of each grid square are (x, y) with 0 <= x, y < 10^6.

We start at the source square and want to reach the target square.  Each move, we can walk to a 4-directionally adjacent square in the grid that isn't in the given list of blocked squares.

Return true if and only if it is possible to reach the target square through a sequence of moves.

 

Example 1:

Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation: 
The target square is inaccessible starting from the source square, because we can't walk outside the grid.
Example 2:

Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation: 
Because there are no blocked cells, it's possible to reach the target square.
"""
# smart math problem
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        bkset=set(map(tuple,blocked))
        flag=set()
        return self.findtarget(bkset,flag,tuple(source),tuple(target),0) and \
               self.findtarget(bkset,flag,tuple(target),tuple(source),0)
    
    def findtarget(self,bkset,flag,source,target,step):
        if step>=20000 or source==target:
            return True
        if source[0]<0 or source[0]>=1000000 or source[1]<0 or source[1]>=1000000 or source in flag or source in bkset:
            return False
        flag.add(source)
        return self.findtarget(bkset,flag,(source[0]+1,source[1]),target,step+1) or \
               self.findtarget(bkset,flag,(source[0]-1,source[1]),target,step+1) or \
               self.findtarget(bkset,flag,(source[0],source[1]+1),target,step+1) or \
               self.findtarget(bkset,flag,(source[0],source[1]-1),target,step+1)
        