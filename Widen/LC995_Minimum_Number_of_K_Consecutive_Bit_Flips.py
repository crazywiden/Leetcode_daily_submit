"""
995. Minimum Number of K Consecutive Bit Flips
In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

 

Example 1:

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].
Example 2:

Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].
Example 3:

Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
"""



# differentiate array 
# https://www.cnblogs.com/grandyang/p/10793594.html
# XOR operation
# use a variable to record how many times have we fliped
# time complexity -- O(N)
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        curr_flip = 0
        res = 0
        is_flip = [0 for _ in range(n)]
        for i in range(n):
            if i >= K:
                curr_flip ^= is_flip[i-K]
            if curr_flip % 2 == A[i]:
                if i + K > n:
                    return -1
                is_flip[i] = 1
                curr_flip ^= 1
                res += 1
        return res
            

# brutal force dfs without pruning
# time complexity -- O(n*2^(n-k))
# TLE
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        s_A = "".join([str(ele) for ele in A])
        return self.dfs(s_A, 0, K, 0)
        
    
    def dfs(self, s, start, k, cnt):
        if s == "1" * len(s):
            return cnt
        if start + k > len(s):
            return -1
        not_flip_cnt = self.dfs(s, start+1, k, cnt)
        
        fliped = s[start:start+k]
        fliped_s = ""
        for i in range(len(s)):
            if i < start or i >= start+ k:
                fliped_s += s[i]
            elif s[i] == "0":
                fliped_s += "1"
            elif s[i] == "1":
                fliped_s += "0"
                
        flip_cnt = self.dfs(fliped_s, start+1, k, cnt+1)
        if flip_cnt == -1:
            return not_flip_cnt
        if not_flip_cnt == -1:
            return flip_cnt
        return min(flip_cnt, not_flip_cnt)


# pruning by element in s
# if s[i] == "1", then don't flip
# if s[i] == "0", the must flip
# time complexity -- O(N^2*K)
# TLE
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        s_A = "".join([str(ele) for ele in A])
        return self.dfs(s_A, 0, K, 0)
        
    
    def dfs(self, s, start, k, cnt):
        if s == "1" * len(s):
            return cnt
        if start + k > len(s):
            return -1
        
        if s[start] == "1":
            not_flip_cnt = self.dfs(s, start+1, k, cnt)
            return not_flip_cnt
        
        fliped = s[start:start+k]
        fliped_s = s[:start]
        for i in range(start, start+k):
            if s[i] == "0":
                fliped_s += "1"
            elif s[i] == "1":
                fliped_s += "0"
        fliped_s += s[start+k:]
        flip_cnt = self.dfs(fliped_s, start+1, k, cnt+1)
        return flip_cnt
    
