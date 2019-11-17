"""
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


# method 1
# time complexity -- O(N^2)
# Runtime: 9000 ms, faster than 5.02% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        for length in range(len(s), 0, -1):
            for i in range(len(s)-length+1):
                l, r = i, i+length-1
                while l<r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l >= r:
                    return s[i:i+length]
        return ""



# method 2 -- central enumeration
# time complexity -- O(N^2)
# Runtime: 1056 ms, faster than 62.07% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, longest = 0, 0
        for middle in range(len(s)):
            # length is odd number
            l, r = middle, middle
            while l<=r and l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if longest < r-l-1:
                longest = r-l-1
                start = l+1
            
            # length is even number
            l, r = middle, middle + 1
            while l<=r and l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if longest < r-l-1:
                longest = r-l-1
                start = l+1
        return s[start:start+longest]


# method 3 -- dp
# Runtime: 4952 ms, faster than 24.09% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 21.3 MB, less than 10.09% of Python3 online submissions for Longest Palindromic Substring.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        # init
        for i in range(n):
            dp[i][i] = True
        for i in range(1, n):
            dp[i][i-1] = True
            
        start, longest = 0, 1
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j] and length > longest:
                    start = i
                    longest = length
        return s[start:start+longest]
    
    