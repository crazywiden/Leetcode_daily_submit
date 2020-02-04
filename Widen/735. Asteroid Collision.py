"""
LC735 Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.
Example 3:
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
"""

# actually very simple stack problem
# took me 2 hours to finish...
# try to think in stack 
# Runtime: 108 ms, faster than 51.60% of Python3 online submissions for Asteroid Collision.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Asteroid Collision.
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for i in range(len(asteroids)):
            if len(res) == 0:
                res.append(asteroids[i])
                continue
                
            # collision will happen
            while len(res) > 0 and asteroids[i] < 0 and res[-1] > 0:
                if -asteroids[i] > res[-1]:
                    res.pop()
                elif -asteroids[i] == res[-1]:
                    res.pop()
                    break
                else:
                    break
            else:
                res.append(asteroids[i])
        return res