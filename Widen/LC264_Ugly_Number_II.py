"""
264. Ugly Number II
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""


# using heap to maintain the order of ugly numbers 
# time complexity -- O(nlogn)
# Runtime: 180 ms, faster than 51.50% of Python3 online submissions for Ugly Number II.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Ugly Number II.
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        visited = set([])
        ugly_nums = [1]
        heapq.heapify(ugly_nums)
        cnt = 1
        while cnt < n:
            base = heapq.heappop(ugly_nums)
            cnt += 1
            if base * 2 not in visited:
                heapq.heappush(ugly_nums, base*2)
                visited.add(base*2)
            if base*3 not in visited:
                heapq.heappush(ugly_nums, base*3)
                visited.add(base*3)
            if base*5 not in visited:
                heapq.heappush(ugly_nums, base*5)
                visited.add(base*5)
        return heapq.heappop(ugly_nums)



# dp 
