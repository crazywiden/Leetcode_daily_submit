"""
72. Edit Distance
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

# normal dp
# Runtime: 204 ms, faster than 41.11% of Python3 online submissions for Edit Distance.
# Memory Usage: 16.3 MB, less than 80.77% of Python3 online submissions for Edit Distance.
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, n_target = len(word1), len(word2)
        if n_target == 0:
            return n
        if n == 0:
            return n_target
        dp = [[0 for _ in range(n_target+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(n_target+1):
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue
                
                if word1[i-1] != word2[j-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1 
                else:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]
                    