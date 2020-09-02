"""
493. Reverse Pairs
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""

# Runtime: 3236 ms, faster than 28.02% of Python3 online submissions for Reverse Pairs.
# Memory Usage: 20.5 MB, less than 67.20% of Python3 online submissions for Reverse Pairs.
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        c = 0
        def divide(nums):
            nonlocal c
            if len(nums) <= 1:
                return nums
            m = len(nums) // 2
            left = divide(nums[:m])
            right = divide(nums[m:])
            i,j = 0, 0
            while i < len(left) and j < len(right):
                if 2 * right[j] >= left[i]:
                    i += 1
                else:
                    c += len(left) - i
                    j += 1
            
            return merge(left, right)
        
        
        def merge(n1, n2):
            res = []
            i,j =0,0
            while i < len(n1) and j < len(n2):
                if n1[i] > n2[j]:
                    res.append(n2[j])
                    j += 1
                else:
                    res.append(n1[i])
                    i += 1
            res.extend(n1[i:] or n2[j:])
            return res
        
        divide(nums)
        
        return c