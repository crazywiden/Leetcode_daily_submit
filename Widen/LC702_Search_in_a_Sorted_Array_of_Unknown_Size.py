"""
LC702 Search in a Sorted Array of Unknown Size
Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.
"""


# Runtime: 36 ms, faster than 97.98% of Python3 online submissions for Search in a Sorted Array of Unknown Size.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Search in a Sorted Array of Unknown Size.
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        start, end = 0, 10000
        while start < end:
            mid = (start + end) // 2
            ele = reader.get(mid)
            if ele == 2147483647 or ele > target:
                end = mid
            elif ele == target:
                return mid
            elif ele < target:
                start = mid + 1
        
        return -1
            
        