"""
516. Longest Palindromic Subsequence
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""


# dp
# difficult part is to get the state transformation formular
# dp[i][j] represent the number of palindromic subsequence in s[i:j]
# if s[i] == s[j], dp[i][j] = 2 + dp[i-1][j-1]
# else dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# Runtime: 1888 ms, faster than 26.99% of Python3 online submissions for Longest Palindromic Subsequence.
# Memory Usage: 30 MB, less than 46.15% of Python3 online submissions for Longest Palindromic Subsequence.

# for such problem, probably traverse length of subsequence is a good idea
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
            
        N = len(s)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            dp[i][i] = 1
        
        for i in range(1, N):
            if s[i] == s[i-1]:
                dp[i-1][i] = 2
            else:
                dp[i-1][i] = 1

        for right in range(2, N):
            for left in range(right-1, -1, -1):
                if s[left] != s[right]:
                    dp[left][right] = max(dp[left+1][right], dp[left][right-1], dp[left][right])
                else:
                    dp[left][right] = 2 + dp[left+1][right-1]

        return dp[0][N-1]
                



