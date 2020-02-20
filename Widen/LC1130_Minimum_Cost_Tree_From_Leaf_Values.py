"""
LC1130 Minimum cost tree from leaf values
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

 

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
"""

# monotonic stack 
# tutor link: https://www.acwing.com/solution/LeetCode/content/3996/
# time complexity -- O(N)
# so brilliant
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        res = 0
        stack = []
        stack.append(float("inf"))
        for ele in arr:
            while ele > stack[-1]:
                tmp = stack.pop()
                res += tmp * min(ele, stack[-1])
            stack.append(ele)
            
        stack.pop(0)
        if len(stack) > 1:
            for i in range(len(stack)-1, 0, -1):
                res += stack[i]*stack[i-1]
        return res
                


# interval dp
# time complexity -- O(n^3)
# Runtime: 280 ms, faster than 21.24% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # interval dp
        n = len(arr)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        dp[0][0] = arr[0]
        for i in range(1, n):
            dp[i][i] = arr[i]
            dp[i-1][i] = arr[i-1] * arr[i]
        for i in range(n-1, -1, -1):
            for j in range(i+2, n):
                min_sum = float("inf")
                for k in range(i, j):
                    tmp = max(arr[i:k+1])*max(arr[k+1:j+1])
                    if i != k:
                        tmp += dp[i][k]
                    if k+1 != j:
                        tmp += dp[k+1][j]
                    min_sum = min(tmp, min_sum)
                dp[i][j] = min_sum
        return dp[0][-1]


