"""
805. Split Array With Same Average
In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)

Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.

Example :
Input: 
[1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
Note:

The length of A will be in the range [1, 30].
A[i] will be in the range of [0, 10000].
"""

# great pruning tricks!
# tutorial: https://www.cnblogs.com/grandyang/p/10285531.html
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        INT_ERROR = 0.00000001
        N = len(A)
        S = sum(A) * 1.0
        target = S / N   
        A = sorted(A)
        for l in range(1, N//2+1):
            if abs(int(l*target) - l*target) > INT_ERROR:
                continue
            if self.helper(A, l, l*target, 0):
                return True
        return False
    
    def helper(self, A, l, S, start):
        if l == 0:
            return abs(S) < 0.00000001
        if A[start] > S / l:
            return False
        for i in range(start, len(A)-l+1):
            if i > start and A[i] == A[i-1]:  # pass duplicated number
                continue
            if self.helper(A, l-1, S-A[i], i+1):
                return True
        return False
    
        
# find a way to transform average to sum. 
# but didn't know how to fully use this idea
# back tracking-- TLE
# time complexity -- O(n!)
class Solution:
    def splitArraySameAverage(self, A) -> bool:
        INT_ERROR = 0.0000001
        S = sum(A)*1.0
        N = len(A)
        target = S / N
        num_freq = Counter(A)
        unique_num = list(num_freq.keys())
        
        for i in range(1, N//2+1):
            if abs(int(i*target) - i*target) > INT_ERROR:
                continue
            if self.helper(int(i*target), unique_num, i, num_freq):
                return True

        return False
    
    def helper(self, S, A, l, num_freq):
        if l == 0:
            if S == 0:
                return True
            return False
        
        for i in range(len(A)):
            if num_freq[A[i]] == 0:
                continue
            num_freq[A[i]] -= 1
            if self.helper(S-A[i], A, l-1, num_freq):
                return True
            num_freq[A[i]] += 1
        return False

# dp solution
# Runtime: 592 ms, faster than 25.00% of Python3 online submissions for Split Array With Same Average.
# Memory Usage: 46.2 MB, less than 15.69% of Python3 online submissions for Split Array With Same Average.
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        N = len(A)
        S = sum(A)
        target = S/N
        dp = [set() for _ in range(N//2+1)]
        dp[0].add(0)
        for num in A:
            for i in range(N//2, 0, -1):
                for ele in dp[i-1]:
                    dp[i].add(ele + num)
        for l in range(1, len(dp)):
            for ele in dp[l]:
                if abs(ele/l-target) < 0.00001:
                    return True
        return False
        
        
        