"""
324. Wiggle Sort II

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""
# O(N) solution
# mapping index method
# so difficult to understand...
# also learns to implement quick select
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        median = self.find_median(nums)  # take O(N)
        # print(median)
        large_idx = 1
        if n % 2 ==0:
            small_idx = n-2
        else:
            small_idx = n-1
        res = [-1 for _ in range(n)]
        for i in range(n):
            if nums[i] > median:
                res[large_idx] = nums[i]
                large_idx += 2
            elif nums[i] < median:
                res[small_idx] = nums[i]
                small_idx -= 2
        for i in range(n):
            if res[i] == -1:
                res[i] = median
        for i in range(n):
            nums[i] = res[i]

    
    def find_median(self, nums):
        n = len(nums)
        k = (n-1) // 2
        left, right = 0, n-1
        while left <= right:
            pivot = left
            pivot_idx = self.partition(nums, left, right, pivot, k)
            dist = pivot_idx - left
            if dist == k:
                return nums[pivot_idx]
            elif dist < k:
                left = pivot_idx + 1
                k -= (dist + 1)
            else:
                right = pivot_idx - 1
    def partition(self, nums, left, right, pivot, k):
        pivot_val = nums[pivot]
        nums[pivot], nums[right] = nums[right], nums[pivot]
        break_p = left
        for i in range(left, right):
            if nums[i] < pivot_val:
                nums[i], nums[break_p] = nums[break_p], nums[i]
                break_p += 1
        nums[break_p], nums[right] = nums[right], nums[break_p]
        return break_p
    
    
    
            
        