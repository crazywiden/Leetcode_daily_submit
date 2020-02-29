"""
10. Regular Expression Matching
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

# similar to decode ways II
# regular dp, just too many cases to be considered
# time complexity could reach O(n_s^2 * n_p)
# because the existence of ".*"
# i am dying...
# Runtime: 56 ms, faster than 52.42% of Python3 online submissions for Regular Expression Matching.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Regular Expression Matching.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n_s, n_p = len(s), len(p)
        if n_p == 0:
            return n_s == 0
        if n_p == 1:
            if n_s == 1 and (s == p or p == "."):
                return True
            return False
                
        dp = [[False for _ in range(n_p+1)] for _ in range(n_s+1)]
        dp[0][0] = True
        for i in range(2, n_p+1, 2):
            if p[i-1] == "*":
                dp[0][i] = dp[0][i-2]
                
        for i in range(1, n_s+1):
            # print(dp)
            for j in range(1, n_p+1):
                if p[j-1] == "*":
                    if p[j-2] != ".":
                        if s[i-1] == p[j-2]:
                            dp[i][j] = dp[i-1][j] or dp[i][j-2]
                        else:
                            dp[i][j] = dp[i][j-2]
                    else:
                        if j == 2:
                            dp[i][j] = True
                        else:
                            for row in range(i+1):
                                dp[i][j] = dp[i][j] or dp[row][j-2]
                elif p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if s[i-1] == p[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = False

        return dp[-1][-1]