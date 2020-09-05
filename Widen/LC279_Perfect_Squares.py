"""
279. Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


# linear search solution space 
# worst time complexity -- O(N * N)
# but because of early stop, converge very fast
class Solution:
    def numSquares(self, n: int) -> int:
        perfect_num = set([i for i in range(1, n+1) if int(math.sqrt(i))**2 == i])
        for cnt in range(1, n+1):
            if self.is_divide(n, cnt, perfect_num):
                return cnt
    
    def is_divide(self, n, k, perfect_num):
        if k == 1:
            return n in perfect_num
        for num in perfect_num:
            if self.is_divide(n-num, k-1, perfect_num):
                return True
        return False


# better dp solution
# time complextity -- O(n^1.5)
# Runtime: 4668 ms, faster than 40.47% of Python3 online submissions for Perfect Squares.
# Memory Usage: 13.9 MB, less than 65.33% of Python3 online submissions for Perfect Squares.

import math
class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] is the least number of perfect square numbers for i 
        dp = [float("inf") for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        perfect_square = set([1])
        for i in range(2, n+1):
            if int(math.sqrt(i))**2 == i:
                dp[i] = 1
                perfect_square.add(i)
                continue
            for j in perfect_square:
                dp[i] = min(dp[i], dp[i-j] + dp[j])
        return dp[-1]


# Runtime: 4732 ms, faster than 5.04% of Python3 online submissions for Perfect Squares.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Perfect Squares.

# dp
# time complextity -- O(n^1.5)
import math
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            largest_square = int(math.sqrt(i))
            if int(math.sqrt(i))**2 == i:
                dp[i] = 1
                continue
            dp[i] = 1 + min([dp[i-j**2] for j in range(1, largest_square+1)])
        return dp[-1]
                
                

# better solutions
# https://leetcode.com/problems/perfect-squares/solution/
# actually very good
# use recursive search
# Runtime: 68 ms, faster than 93.15% of Python3 online submissions for Perfect Squares.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Perfect Squares.
class Solution:
    def numSquares(self, n: int) -> int:
        self.squares = set([i*i for i in range(int(math.sqrt(n))+1)])
        for cnt in range(1, n+1):
            if self.divide(n, cnt):
                return cnt

    def divide(self, n, k):
        if k == 1:
            return n in self.squares
        
        for square in self.squares:
            if self.divide(n-square, k-1):
                return True
        return False





