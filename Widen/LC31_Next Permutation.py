"""
31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

# Runtime: 40 ms, faster than 70.51% of Python3 online submissions for Next Permutation.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Next Permutation.
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = len(nums)-2, len(nums)-1
        while nums[left] >= nums[right]:
            left -= 1
            right -= 1
            if left < 0:
                break
        if left >= 0:
            while nums[left] < nums[right]:
                right += 1 
                if right == len(nums):
                    break
            nums[left], nums[right-1] = nums[right-1], nums[left]
        
        nums[left+1:] = nums[left+1:][::-1]