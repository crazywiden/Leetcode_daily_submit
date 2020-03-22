"""
977. Squares of a Sorted Array
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

# two pointer solution
# tutorial: https://leetcode.com/articles/squares-of-a-sorted-array/
# should be O(N) solution
# but slower than built-in sorted()
# Runtime: 276 ms, faster than 26.58% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 14.8 MB, less than 94.05% of Python3 online submissions for Squares of a Sorted Array.
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if len(A) == 0:
            return []
        neg, pos = 0, 0
        while pos < len(A) and A[pos] <= 0:
            pos += 1
        neg = pos - 1
        res = []
        while neg >= 0 and pos < len(A):
            if abs(A[pos]) < abs(A[neg]):
                res.append(A[pos]**2)
                pos += 1
            else:
                res.append(A[neg]**2)
                neg -= 1
            
        while neg >= 0:
            res.append(A[neg]**2)
            neg -= 1
        
        while pos < len(A):
            res.append(A[pos]**2)
            pos += 1
        return res
    


# a little bit optimization of the raw sorted solution
# overall should be O(nlogn) solution
# Runtime: 252 ms, faster than 45.94% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 15 MB, less than 79.76% of Python3 online submissions for Squares of a Sorted Array.
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if len(A) == 0:
            return []
        
        is_first_nega = False
        if A[0] < 0:
            is_first_nega = True
        res = []
        for i in range(len(A)):
            if abs(A[i]) > abs(A[0]) and is_first_nega:
                res = sorted(res)
                is_first_nega = False
            res.append(A[i]**2)
        if is_first_nega:
            return sorted(res)
        return res
    
        