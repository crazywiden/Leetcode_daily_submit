"""
172. Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""
# easy 
# Runtime: 20 ms, faster than 97.13% of Python3 online submissions for Factorial Trailing Zeroes.
# Memory Usage: 14 MB, less than 10.00% of Python3 online submissions for Factorial Trailing Zeroes.
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        base = 5
        while base <= n:
            res += n // base
            base *= 5
        return res
    