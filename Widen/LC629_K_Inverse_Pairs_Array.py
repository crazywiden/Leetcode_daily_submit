"""
629. K Inverse Pairs Array

Given two integers n and k, find how many different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.

We define an inverse pair as following: For ith and jth element in the array, if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.

Since the answer may be very large, the answer should be modulo 109 + 7.

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: 
Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.
 

Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: 
The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
"""

# so smart to use dp!!
# so smart for the transition function!
# tutorial: https://www.cnblogs.com/grandyang/p/7111385.html
# Runtime: 560 ms, faster than 43.42% of Python3 online submissions for K Inverse Pairs Array.
# Memory Usage: 167.2 MB, less than 100.00% of Python3 online submissions for K Inverse Pairs Array.
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MAX_INT = 10**9 + 7
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            dp[i][0] = 1
            for j in range(1, k+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                if j >= i:
                    dp[i][j] -= dp[i-1][j-i]
        return dp[-1][-1] % MAX_INT
    



