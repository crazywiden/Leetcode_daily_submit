"""
862. Shortest Subarray with Sum at Least K
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
"""

# Runtime: 1196 ms, faster than 9.86% of Python3 online submissions for Shortest Subarray with Sum at Least K.
# Memory Usage: 19.2 MB, less than 25.00% of Python3 online submissions for Shortest Subarray with Sum at Least K.
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        prefix_sum = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + A[i-1]
        
        deque = []  # store index of elements
        res = n+1
        for idx, val in enumerate(prefix_sum):
            while len(deque) > 0 and val < prefix_sum[deque[-1]]:
                deque.pop()
            
            while len(deque) > 0 and val - prefix_sum[deque[0]] >= K:
                res = min(res, idx-deque[0])
                deque.pop(0)
                
            deque.append(idx)
            
        if res == n+1:
            return -1
        return res
        