"""
1249. Minimum Remove to Make Valid Parentheses
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
"""
# two pass solution
# first pass:
# record what indices are extra
# second pass:
# skip the indices marked
# Runtime: 164 ms, faster than 34.23% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        skip_indices = self.get_skip(s)
        res = ""
        for i in range(len(s)):
            if i in skip_indices:
                continue
            res += s[i]
        return res
    
    def get_skip(self, s):
        res = set([])
        stack = []
        for i in range(len(s)):
            if s[i] == ")":
                if len(stack) == 0 or stack[-1][0] != "(":
                    res.add(i)
                elif stack[-1][0] == "(":
                    stack.pop()
            elif s[i] == "(":
                stack.append([s[i], i])
        for i in range(len(stack)):
            res.add(stack[i][1])
        return res


# another two pass algorithm
# first pass: remove all invalid ")"
# second pass: remove all invalid "("
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = self.remove_invalid(s, "(", ")")
        s = self.remove_invalid(s[::-1], ")", "(")
        return s[::-1]
    
    def remove_invalid(self, s, left_str, right_str):
        left_cnt, right_cnt = 0, 0
        res = ""
        for i in range(len(s)):
            if s[i] == right_str:
                if left_cnt == 0:
                    right_cnt += 1
                    continue
                else:
                    left_cnt -= 1
            elif s[i] == left_str:
                left_cnt += 1
            res += s[i]
        return res
        
        