"""
265. Paint House II
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
Follow up:
Could you solve it in O(nk) runtime?
"""


# classical dp
# time complexity -- O(n*k^2)
# Runtime: 212 ms, faster than 22.55% of Python3 online submissions for Paint House II.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Paint House II.
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        if len(costs[0]) == 0:
            return 0
        n, k = len(costs), len(costs[0])
        dp = [[0 for _ in range(k)] for _ in range(n)]
        for j in range(k):
            dp[0][j] = costs[0][j]
        
        for i in range(1, n):
            for j in range(k):
                min_val = float("inf")
                for t in range(k):
                    if t == j:
                        continue
                    min_val = min(min_val, dp[i-1][t])
                dp[i][j] = min_val + costs[i][j]
        return min(dp[-1])
                