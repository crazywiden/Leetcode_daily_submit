"""
LC338 --  Counting Bits
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""


# think of this method myself
# Runtime: 88 ms, faster than 52.85% of Python3 online submissions for Counting Bits.
# Memory Usage: 20.7 MB, less than 5.00% of Python3 online submissions for Counting Bits.
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0 for _ in range(1+num)]
        gap = 1
        for i in range(1, num+1):
            if i >= gap*2:
                gap *= 2
            res[i] = res[i-gap] + 1 
        return res


# relatively easy... but more advanced method need knowledge of bit operation
# Runtime: 100 ms, faster than 57.44% of Python3 online submissions for Counting Bits.
# Memory Usage: 19.9 MB, less than 5.00% of Python3 online submissions for Counting Bits.
# time complexity -- O(N)
# space complexity -- O(N)
class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        dp = [0 for _ in range(num+1)]
        dp[1] = 1
        for i in range(2, num+1):
            dp[i] = dp[i//2] + dp[i%2]
        return dp

