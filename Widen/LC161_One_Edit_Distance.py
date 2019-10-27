"""
LC161 - One Edit Distance
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
"""

# easy one
# Runtime: 36 ms, faster than 84.44% of Python3 online submissions for One Edit Distance.
# Memory Usage: 13.9 MB, less than 14.29% of Python3 online submissions for One Edit Distance.
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        if s == t:
            return False
        
        # check replace
        if len(s) == len(t):
            diff_cnt = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    diff_cnt += 1
                    if diff_cnt > 1:
                        return False
            return True
        
        # delete and insert are essentially the same
        diff_cnt = 0
        s_ptr, t_ptr = 0, 0
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] != t[t_ptr]:
                diff_cnt += 1
                if diff_cnt > 1:
                    return False
                if len(s) > len(t):
                    s_ptr += 1
                else:
                    t_ptr += 1
            else:
                s_ptr += 1
                t_ptr += 1
        return True
            
        