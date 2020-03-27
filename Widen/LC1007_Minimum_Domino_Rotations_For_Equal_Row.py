"""
1007. Minimum Domino Rotations For Equal Row
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.
"""

# I am so hate greedy method!!
# tutorial: https://leetcode.com/articles/minimum-domino-rotations-for-equal-row/
# Runtime: 1160 ms, faster than 93.49% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # greedy!!!
        # one can only make A[0] or B[0]
        # two pass solution
        if len(A) == 1:
            return 0
        res_a = self.check(A, B, A[0])
        res_b = self.check(A, B, B[0])
        if res_a == -1:
            return res_b
        if res_b == -1:
            return res_a
        return min(res_a, res_b)
    
    def check(self, A, B, val):
        n = len(A)
        res_a, res_b = 0, 0
        for i in range(n):
            if A[i] != val and B[i] != val:
                return -1
            if A[i] != val:
                res_a += 1
            elif B[i] != val:
                res_b += 1
        
        return min(res_a, res_b)
    
        
        
