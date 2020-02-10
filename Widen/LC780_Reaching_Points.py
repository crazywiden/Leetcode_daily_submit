"""
780. Reaching Points
A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:

sx, sy, tx, ty will all be integers in the range [1, 10^9].
"""
# this problem is a great excercise for time complexity analysis
# need to know Euclidean algorithm -- an algorithm used to find the gcd of two numbers
# time complexity of Euclidean algorithm is O(log(a+b))
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            
            if tx > ty:
                if ty > sy:
                    tx = tx % ty
                else: # in this case ty == sy
                     # only tx will change
                     # and it can only change by subtracting by ty
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty = ty % tx
                else: # in this case tx == sx
                    return (ty - sy) % tx == 0
        return tx == sx and ty == sy

# basic dp and bfs
# turns out memeory limit exceed
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False
        
        dp = [[False for _ in range(ty+1)] for _ in range(tx+1)]
        stack = [[sx, sy]]
        while len(stack) > 0:
            x, y = stack.pop(0)
            new_x1, new_y1 = x, x+y
            new_x2, new_y2 = x+y, y
            if self.check(new_x1, new_y1, tx, ty):
                dp[new_x1][new_y1] = True
                stack.append([new_x1, new_y1])
            if self.check(new_x2, new_y2, tx, ty):
                dp[new_x2][new_y2] = True
                stack.append([new_x2, new_y2])
        return dp[-1][-1]
    
    def check(self, new_x, new_y, tx, ty):
        return 0<=new_x<=tx and 0<=new_y<=ty 

# if change to this
# time limit exceed
# time complexity for this senario is actually O(2^(tx + ty))

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False
        
        stack = [[sx, sy]]
        while len(stack) > 0:
            x, y = stack.pop(0)
            new_x1, new_y1 = x, x+y
            new_x2, new_y2 = x+y, y
            if self.check(new_x1, new_y1, tx, ty):
                if new_x1 == tx and new_y1 == ty:
                    return True
                stack.append([new_x1, new_y1])
            if self.check(new_x2, new_y2, tx, ty):
                if new_x2 == tx and new_y2 == ty:
                    return True
                stack.append([new_x2, new_y2])
        return False
    
    def check(self, new_x, new_y, tx, ty):
        return 0<=new_x<=tx and 0<=new_y<=ty 
    

35
13
455955547
420098884
    