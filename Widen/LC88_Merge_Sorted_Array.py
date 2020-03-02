"""
88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
# Runtime: 28 ms, faster than 95.75% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return 
        if n == 0:
            return 
        
        p1, p2 = m-1, n-1
        res_p = m + n - 1 
        while p1 >=0 and p2>=0:
            if nums1[p1] < nums2[p2]:
                nums1[res_p] = nums2[p2]
                p2 -= 1
            else:
                nums1[res_p] = nums1[p1]
                p1 -= 1
            res_p -= 1
        
        while p2 >= 0:
            nums1[p2] = nums2[p2]
            p2 -= 1
            
            
        