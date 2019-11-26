"""
162. Find Peak Element
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
"""


# detect 4 patterns
# time complexity -- O(logN)
# Runtime: 44 ms, faster than 94.35% of Python3 online submissions for Find Peak Element.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Find Peak Element.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 2:
            if nums[1] > nums[0]:
                return 1
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid == 0 and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid-1] < nums[mid] < nums[mid+1]:
                left = mid + 1
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                right = mid
            elif nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            else:
                left = mid+1
        return len(nums)-1



        
        
        
        
        
        
        
        
        
        
         
        
        
        
        
        
        
        
        
