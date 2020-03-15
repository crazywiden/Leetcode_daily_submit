"""
1043. Partition Array for Maximum Sum
Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

 

Example 1:

Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]
 

Note:

1 <= K <= A.length <= 500
0 <= A[i] <= 10^6
"""
# method 2: interval dp
# for array partition problem, should first think of interval dp
# Runtime: 1172 ms, faster than 27.97% of Python3 online submissions for Partition Array for Maximum Sum.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Partition Array for Maximum Sum.
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0 for _ in range(n)]
        init_max = float("-inf")
        for i in range(K):
            init_max = max(init_max, A[i])
            dp[i] = init_max * (i+1)
        
        for i in range(K, n):
            curr_max = float("-inf")
            for l in range(1, K+1):
                curr_max = max(curr_max, dp[i-l] + l*max(A[i-l+1:i+1]))
            dp[i] = curr_max
        return dp[-1]
        
# method 1: dfs with memorization 
# time complexity -- O(N*K)
# space complexity -- O(N)
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        # partition an array
        # should first think of interval dp
        
        # dfs with memeorization
        self.memo = {} # key is the start index, value is maximum sum
        n = len(A)
        res = 0
        for i in range(1, K+1):
            tmp = max(A[:i])*i + self.dfs(A, i, K)
            res = max(res, tmp)
        # print(self.memo)
        return res
    
    def dfs(self, A, start, K):
        if start in self.memo:
            return self.memo[start]
        if start >= len(A):
            return 0
        res = 0
        for l in range(1, K+1):
            if start + l > len(A):
                break
            tmp = max(A[start:start+l])*l + self.dfs(A, start+l, K)
            res = max(res, tmp)
        self.memo[start] = res
        return res
    
        
