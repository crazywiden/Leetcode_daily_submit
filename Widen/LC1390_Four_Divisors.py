"""
1390. Four Divisors
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
"""

# don't mess up with divisor and prime divisors
# Runtime: 2128 ms, faster than 100.00% of Python3 online submissions for Four Divisors.
# Memory Usage: 22 MB, less than 100.00% of Python3 online submissions for Four Divisors.
import collections
import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        self.memo = {}
        res = 0
        for val in nums:
            divisors = self.find_divisor(val)
            # print(divisors, val)
            if len(divisors) == 4:
                res += sum(divisors)
        return res
    
    def find_divisor(self, val):
        root = val
        res = set([1, val])
        divisor = 2
        upper_bound = math.sqrt(val)
        while divisor <= upper_bound:
            if root % divisor == 0:
                val = root // divisor
                if val in self.memo:
                    extra = self.memo[val].copy()
                    res.add(divisor)
                    res = res.union(extra)
                    self.memo[root] = res
                    return res
                res.add(divisor)
                res.add(val)
            divisor += 1
            
        self.memo[root] = res
        return res
        