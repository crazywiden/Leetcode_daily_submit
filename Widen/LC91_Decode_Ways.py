"""
LC 91 decode ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

# original dp, similar to climb stairs but need to consider the case of "0"
# Runtime: 32 ms, faster than 59.50% of Python3 online submissions for Decode Ways.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Decode Ways.

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        if s[0] == "0":
            return 0
        if n == 1:
            return 1
        
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        for i in range(1, n+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if s[i-1] >= "0" and s[i-1] <= "6":
                if s[i-2] == "1" or s[i-2] == "2":
                    dp[i] += dp[i-2]
            elif s[i-2] == "1":
                dp[i] += dp[i-2]
                
        return dp[-1]

# optimization on memeory, significant speed improvement
# Runtime: 28 ms, faster than 83.56% of Python3 online submissions for Decode Ways.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Decode Ways.
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        if s[0] == "0":
            return 0
        if n == 1:
            return 1
        

        prev, now = 0, 1
        for i in range(1, n+1):
            tmp = 0
            if s[i-1] != "0":
                tmp += now
            if s[i-1] >= "0" and s[i-1] <= "6":
                if s[i-2] == "1" or s[i-2] == "2":
                    tmp += prev
            elif s[i-2] == "1":
                tmp += prev
            prev, now = now, tmp
                
        return now
                

                
                    