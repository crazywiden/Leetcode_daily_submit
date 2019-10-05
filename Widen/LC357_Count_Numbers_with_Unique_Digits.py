"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
"""
# time complexity -- 0(N)
# space complexity -- O(1)
# Runtime: 32 ms, faster than 88.89% of Python3 online submissions for Count Numbers with Unique Digits.
# Memory Usage: 13.9 MB, less than 50.00% of Python3 online submissions for Count Numbers with Unique Digits.



class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        last_digit = 10
        curr_digit = 9 * 9 
        cnt = last_digit + curr_digit
        for i in range(3, n+1):
            last_digit = curr_digit
            curr_digit = last_digit * (9-i+2)
            cnt += curr_digit
        return cnt
        
        


