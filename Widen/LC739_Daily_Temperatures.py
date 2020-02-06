"""
LC739 daily temperature
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

# use monotonic stack to solve
# just a variant of find maximum drawdown in O(N)
# Runtime: 528 ms, faster than 37.83% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Daily Temperatures.
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        stack = [n-1]
        res = [0 for _ in range(n)]
        for i in range(n-1, -1, -1):
            while len(stack) != 0 and T[stack[-1]] <= T[i]:
                stack.pop()
            if len(stack) != 0:
                res[i] = stack[-1] - i
            stack.append(i)
        return res