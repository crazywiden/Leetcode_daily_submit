"""
LC4. Median of Two Sorted Arrays
"""

# Runtime: 88 ms, faster than 98.80% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)  # 合并排序
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        else:
            return nums[len(nums) // 2]