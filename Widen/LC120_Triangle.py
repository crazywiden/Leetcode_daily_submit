"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""


# simple dp
# time complexity -- O(N^2)
# Runtime: 60 ms, faster than 92.08% of Python3 online submissions for Triangle.
# Memory Usage: 13.5 MB, less than 86.67% of Python3 online submissions for Triangle.
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_dp = [0 for _ in range(len(triangle))]
        dp = [0 for _ in range(len(triangle))]
        dp[0] = triangle[0][0]
        prev_dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[j] = triangle[i][j] + prev_dp[j]
                elif j == i:
                    dp[j] = triangle[i][j] + prev_dp[j-1]
                    break
                else:
                    dp[j] = triangle[i][j] + min(prev_dp[j], prev_dp[j-1])
            prev_dp = dp.copy()
        return min(dp)