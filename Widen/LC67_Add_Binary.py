"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


# kind of cheating since I used a lot of build-in function
# Runtime: 28 ms, faster than 99.51% of Python3 online submissions for Add Binary.
# Memory Usage: 14 MB, less than 5.41% of Python3 online submissions for Add Binary.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0:
            if len(b) == 0:
                return "0"
            return b
        if len(b) == 0:
            return a
        
        res = int(a, 2) + int(b, 2)
        return str(bin(res))[2:]
        