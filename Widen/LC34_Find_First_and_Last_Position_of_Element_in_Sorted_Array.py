"""
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

# find target first then spread to both side
# time complexity -- O(N)
# Runtime: 168 ms, faster than 6.29% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 14 MB, less than 21.43% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid
                break
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if nums[left] != target:
            return [-1, -1]
        res = [left, left]
        right = left
        while left >= 0 and nums[left] == target:
            left -= 1
        while right < len(nums) and nums[right] == target:
            right += 1
        return [left+1, right-1]


# spread to both side in linear manner is too slow
# first find the left most element then find the right most element
# time complexity -- O(logN)
# Runtime: 92 ms, faster than 86.50% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 13.9 MB, less than 32.14% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        res = [-1, -1]
        # find the first position
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if (mid == 0 or nums[mid] > nums[mid-1]) and (nums[mid] == target):
                res[0] = mid
                left = mid
                break
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] != target:
            return [-1, -1]
        else:
            res[0] = left
        
        # find the right position
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if (mid == len(nums)-1 or nums[mid] < nums[mid+1]) and (nums[mid] == target):
                res[1] = mid
                right = mid
                break
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[right] == target:
            res[1] = right
        return res
            

        


