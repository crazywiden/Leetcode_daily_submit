"""
801. Minimum Swaps To Make Sequences Increasing

We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: 
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
Note:

A, B are arrays with the same length, and that length will be in the range [1, 1000].
A[i], B[i] are integer values in the range [0, 2000].
"""
# dp
# should definitely practice more on dp
# Runtime: 100 ms, faster than 24.48% of Python3 online submissions for Minimum Swaps To Make Sequences Increasing.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Minimum Swaps To Make Sequences Increasing.
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        dp = [[n+1 for _ in range(n)] for _ in range(2)]
        dp[0][0] = 0
        dp[1][0] = 1
        for i in range(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                dp[0][i] = min(dp[0][i], dp[0][i-1])
                dp[1][i] = min(dp[1][i], dp[1][i-1]) + 1
            
            if A[i] > B[i-1] and B[i] > A[i-1]:
                dp[0][i] = min(dp[0][i], dp[1][i-1])
                dp[1][i] = min(dp[1][i], dp[0][i-1]+1)
        return min(dp[0][-1], dp[1][-1])


# rolling array to decrease memory complexity
# Runtime: 92 ms, faster than 63.08% of Python3 online submissions for Minimum Swaps To Make Sequences Increasing.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Minimum Swaps To Make Sequences Increasing.
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        dp = [[n+1 for _ in range(2)] for _ in range(2)]
        now, old = 0, 1
        dp[0][now] = 0
        dp[1][now] = 1
        for i in range(1, n):
            old = now
            now = 1 - now
            dp[0][now], dp[1][now] = n+1, n+1
            if A[i] > A[i-1] and B[i] > B[i-1]:
                dp[0][now] = dp[0][old]
                dp[1][now] = dp[1][old] + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                dp[0][now] = min(dp[0][now], dp[1][old])
                dp[1][now] = min(dp[1][now], dp[0][old]+1)
        return min(dp[0][now], dp[1][now])
    