"""
LC338 --  Counting Bits
relatively easy... but more advanced method need knowledge of bit operation
Runtime: 100 ms, faster than 57.44% of Python3 online submissions for Counting Bits.
Memory Usage: 19.9 MB, less than 5.00% of Python3 online submissions for Counting Bits.
time complexity -- O(N)
space complexity -- O(N)
"""
class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        dp = [0 for _ in range(num+1)]
        dp[1] = 1
        for i in range(2, num+1):
            dp[i] = dp[i//2] + dp[i%2]
        return dp

