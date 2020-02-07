"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

# dfs again
# Runtime: 32 ms, faster than 47.73% of Python3 online submissions for Combination Sum III.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Combination Sum III.
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 10))
        level = 0
        res = []
        self.dfs(res, [], candidates, n, level, k)
        return res
    
    def dfs(self, res, tmp, A, target, level, k):
        if level > k:
            return 
        if target < 0:
            return 
        if target == 0 and level == k:
            res.append(tmp.copy())
            return 
        
        for i in range(len(A)):
            tmp.append(A[i])
            level += 1 
            self.dfs(res, tmp, A[i+1:], target-A[i], level, k)
            tmp.pop()
            level -= 1
            