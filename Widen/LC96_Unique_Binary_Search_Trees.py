"""
96. Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# after look at the <introduction to algorithms>
# do this problem easy piece
# Runtime: 28 ms, faster than 59.27% of Python3 online submissions for Unique Binary Search Trees.
# Memory Usage: 14 MB, less than 10.71% of Python3 online submissions for Unique Binary Search Trees.
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            cnt = 0
            for root in range(1, i+1):
                cnt += dp[root-1] * dp[i-root]
            dp[i] = cnt
        return dp[-1]
    