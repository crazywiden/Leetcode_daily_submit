"""
639. Decode Ways II
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.
"""

# that's hard
# hard to enumerate all cases

# Runtime: 1492 ms, faster than 22.18% of Python3 online submissions for Decode Ways II.
# Memory Usage: 342 MB, less than 50.00% of Python3 online submissions for Decode Ways II.
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == "0":
            return 0  
        if n == 1:
            if s[0] == "*":
                return 9 
            return 1 
            
        mod = 10**9 + 7
        dp = [0 for _ in range(n)]
        
        if s[0] == "*":
            dp[0] = 9
        else:
            dp[0] = 1 
        
        if s[1] == "*":
            if s[0] == "*":
                dp[1] = 9 + 6 + 81 
            elif s[0] == "1":
                dp[1] = 9 + 9
            elif s[0] == "2":
                dp[1] = 6 + 9
            else:
                dp[1] = 9 
        elif s[1] == "0":
            if s[0] == "1" or s[0] =="2":
                dp[1] = 1
            elif s[0] == "*":
                dp[1] = 2
            else:
                dp[1] = 0 
        elif "1" <= s[1] <= "6":
            if s[0] == "1" or s[0] == "2":
                dp[1] = 2 
            elif s[0] == "*":
                dp[1] = 9 + 2 
            else:
                dp[1] = 1
        else:
            if s[0] == "*":
                dp[1] = 9 + 1 
            elif s[0] == "1":
                dp[1] = 2 
            else:
                dp[1] = 1 
                
        for i in range(2, n):
            if s[i] == "*":
                dp[i] += 9 * dp[i-1]
                if s[i-1] == "1":
                    dp[i] += dp[i-2] *9 
                elif s[i-1] == "2":
                    dp[i] += dp[i-2] * 6
                elif s[i-1] == "*":
                    dp[i] += dp[i-2] * 15
                    
            elif s[i] == "0":
                if s[i-1] in ["1", "2"]:
                    dp[i] = dp[i-2]
                elif s[i-1] == "*":
                    dp[i] = dp[i-2] * 2
            elif "1" <= s[i] <= "6":
                dp[i] += dp[i-1]
                if s[i-1] in ["1", "2"]:
                    dp[i] += dp[i-2]
                elif s[i-1] == "*":
                    dp[i] += dp[i-2] * 2  
            else:
                dp[i] += dp[i-1]
                if s[i-1] == "1" or s[i-1] == "*":
                    dp[i] += dp[i-2]
        
        return dp[-1] % mod 