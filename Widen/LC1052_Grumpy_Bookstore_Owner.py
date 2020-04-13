"""
1052. Grumpy Bookstore Owner
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
"""

# prefix sum  -- window sum
# the space complexity can be further optimized using only one variable to represent the window sum
# time complexity -- O(N)
# Runtime: 304 ms, faster than 81.61% of Python3 online submissions for Grumpy Bookstore Owner.
# Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Grumpy Bookstore Owner.
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        base_satisfied = 0
        prefix_sum_grumpy = [0 for _ in range(n+1)]
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfied += customers[i]
                prefix_sum_grumpy[i+1] = prefix_sum_grumpy[i]
            else:
                prefix_sum_grumpy[i+1] = prefix_sum_grumpy[i] + customers[i]
        # print(prefix_sum_grumpy)
        res = base_satisfied
        for i in range(n):
            if i+X <= n:
                extra = prefix_sum_grumpy[i+X] - prefix_sum_grumpy[i]
                res = max(res, base_satisfied + extra)
        return res
    