"""
LC829
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
"""

# just a math problem
# Runtime: 104 ms, faster than 77.95% of Python3 online submissions for Consecutive Numbers Sum.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Consecutive Numbers Sum.
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        
        res = 0
        numerator = 2*N
        upper = int(math.sqrt(numerator))
        for l in range(upper+1):
            if numerator % (l+1) == 0:
                k = numerator//(l+1) - l
                if k % 2 == 0 and k != 0:
                    res += 1 
        return res
    
    