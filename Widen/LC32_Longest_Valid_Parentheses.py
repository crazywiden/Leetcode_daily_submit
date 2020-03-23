"""
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

# actually very simple
# please calm down and think about different categories 
# Runtime: 48 ms, faster than 42.22% of Python3 online submissions for Longest Valid Parentheses.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Valid Parentheses.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [0 for _ in range(n)]
        for i in range(1, n):
            if s[i] == ")":
                if s[i-1] == "(":
                    if i >= 2:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                else:
                    if i > dp[i-1] and s[i-dp[i-1]-1] == "(":
                        dp[i] = dp[i-1] + 2
                        if i-dp[i-1]-2 >= 0:
                            dp[i] += dp[i-dp[i-1]-2]
                        
            res = max(res, dp[i])
            
        return res
                        

# looks simple but actually hard
# TLE solution
# time complexity -- O(N^2)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        memo = {(i,i):[s[i]] for i in range(n)}
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                memo[(i, j)] = memo[(i, j-1)].copy()
                if len(memo[(i, j)]) == 0:
                    memo[(i, j)].append(s[j])
                    continue
                    
                if s[j] == ")" and memo[(i, j)][-1] == "(":
                    memo[(i, j)].pop()
                else:
                    memo[(i, j)].append(s[j])
                    
                if len(memo[(i, j)]) == 0:
                    res = max(res, j-i+1)
        return res