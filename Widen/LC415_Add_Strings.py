"""
415. Add Strings
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""



# Runtime: 472 ms, faster than 5.60% of Python3 online submissions for Add Strings.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Add Strings.
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) == 0:
            return num2
        if len(num2) == 0:
            return num1 
        tot = self.str2num(num1) + self.str2num(num2)
        return self.num2str(tot)
    
    def str2num(self, num):
        level = 0
        n = len(num)
        res = 0
        for i in range(n-1, -1, -1):
            res += (ord(num[i]) - ord("0")) * 10**level
            level += 1
        return res
    
    def num2str(self, num):
        res = ""
        if num == 0:
            return "0"
        while num > 0:
            r = num % 10
            res = str(r) + res
            num = num // 10
        return res
        
        
        
        