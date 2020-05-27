"""
718. Maximum Length of Repeated Subarray
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
 

Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""
# simple dp
# time complexity -- O(N^2)
# Runtime: 4720 ms, faster than 47.10% of Python3 online submissions for Maximum Length of Repeated Subarray.
# Memory Usage: 40.1 MB, less than 16.67% of Python3 online submissions for Maximum Length of Repeated Subarray.
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n_A, n_B = len(A), len(B)
        dp = [[0 for _ in range(n_A)] for _ in range(n_B)]
        res = 0
        for i in range(n_A):
            if B[-1] == A[i]:
                dp[-1][i] = 1
                res = 1
        for i in range(n_B):
            if A[-1] == B[i]:
                dp[i][-1] = 1
                res = 1
        
        for i in range(n_B-2, -1, -1):
            for j in range(n_A-2, -1, -1):
                if B[i] != A[j]:
                    continue
                dp[i][j] = 1 + dp[i+1][j+1]
                res = max(res, dp[i][j])
        return res
    
        