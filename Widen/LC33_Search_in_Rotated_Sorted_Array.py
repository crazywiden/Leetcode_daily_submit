"""
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
# binary search
# time complexity -- O(logn)
Runtime: 36 ms, faster than 97.21% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                if nums[mid] < nums[-1]:
                    if target < nums[-1]:
                        left = mid + 1
                    else:
                        right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] > nums[-1]:
                    if target > nums[-1]:
                        right = mid
                    else:
                        left = mid + 1
                else:
                    right = mid
                    
        if nums[left] == target:
            return left
        return -1


# also there is a solution of two pass
# first find the pivot then compare target and nums[pivot] to get a monotonic sequence
# perform binay search on that monotonic sequence
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
                
        def search(left, right):
            """
            Binary search
            """
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1
        
        n = len(nums)
        
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1 
        
        rotate_index = find_rotate_index(0, n - 1)
        
        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n - 1)
        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n - 1)
        # search on the left side
        return search(0, rotate_index)

                
                