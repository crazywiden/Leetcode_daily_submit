"""
696. Count Binary Substrings
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
"""
# so annoying... 
# Runtime: 188 ms, faster than 43.52% of Python3 online submissions for Count Binary Substrings.
# Memory Usage: 13.4 MB, less than 33.33% of Python3 online submissions for Count Binary Substrings.
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        num_zero, num_one = 0, 0
        res = 0
        idx = 0
        n = len(s)
        while idx < n:
            num_zero = 0
            while idx < n and s[idx] == "0":
                num_zero += 1
                idx += 1
            res += min(num_zero, num_one)
            num_one = 0
            while idx < n and s[idx] == "1":
                num_one += 1
                idx += 1
            res += min(num_zero, num_one)
        return res
    
            