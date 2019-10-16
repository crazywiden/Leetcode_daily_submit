"""
LC829 Consecutive number sum
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
"""

# hard math problem...


# native approach -- brutal force
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        cnt  = 0
        for i in range(len(N)):
            for j in range(i+1, len(N)):
                sub_sum = (i +j)*(j-i+1)/2
                if sub_sum > N:
                    break
                elif sub_sum == N:
                    cnt +=1
                    break
        return cnt + 1



# find existence 
# used summation formula of arthmetic series
# Runtime: 480 ms, faster than 5.14% of Python3 online submissions for Consecutive Numbers Sum.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Consecutive Numbers Sum.
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        cnt = 0
        for m in range(1, N+1):
            mx = N + 0.5 * (m - m**2)
            if mx <= 0:
                break
            if mx != int(mx):
                continue
            if mx % m == 0:
                cnt += 1
        return cnt




# not figure it out now...
# If N = i * j, then we want to find i consecutive numbers with average j
# For example, 15 = 3 * 5, then 4 + 5 + 6, 3 numbers with average 5; 
# and 15 = 5 * 3, then 1 + 2 + 3 + 4 + 5, 5 numbers with average 3
# But one constraint is that i must be odd, since if i is even k + 1, k + 2, ... k + i. 
# The average = (ik + (1 + i)*i/2) / i = k + (1 + i) / 2, cannot be an integer.
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        if N == 1: 
            return 1
        res = 1
        for i in range(2, int(N ** .5 + 1)):   
            if N % i == 0:
                if i % 2 == 1: # If i is odd, then we can form a sum of length i
                    res += 1
                j = (N // i) # Check the corresponding N // i
                if i != j and j % 2 == 1:
                    res += 1
        if N % 2 == 1: # If N is odd(2k + 1). Then N = k + k + 1, not included above
            res += 1
        
        return res
                
                





