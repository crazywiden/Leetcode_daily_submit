"""
440. K-th Smallest in Lexicographical Order
Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
"""


# brilliant idea
# time complexity -- O(log N)
# Runtime: 32 ms, faster than 41.88% of Python3 online submissions for K-th Smallest in Lexicographical Order.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for K-th Smallest in Lexicographical Order.
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        if n < 10:
            return k
        res = 1
        k -= 1 
        while k > 0:
            gap = self.find_gap(n, res, res+1)
            if k >= gap:
                k -= gap 
                res += 1 
            else:
                k -= 1
                res *= 10 
        return res 
    
    def find_gap(self, n, left, right):
        gap = 0
        while left <= n:
            gap += min(n+1, right) - left
            left *= 10
            right *= 10
        return gap
    
        
    

# use similar ideas to LC386
# TLE
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        for i in range(k):
            res = curr
            if curr*10 <= n:
                curr *= 10
            else:
                if curr >= n:
                    curr = curr // 10
                curr += 1
                while curr % 10 == 0:
                    curr /= 10 
        return int(res)
    