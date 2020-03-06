"""
280. Wiggle Sort
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
"""
# greedy
# Runtime: 100 ms, faster than 51.27% of Python3 online submissions for Wiggle Sort.
# Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Wiggle Sort.
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        while idx < len(nums) - 1:
            if idx % 2 ==0:
                if nums[idx] > nums[idx+1]:
                    nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
            else:
                if nums[idx] < nums[idx+1]:
                    nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
            idx += 1
            