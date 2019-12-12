"""
238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
# Runtime: 128 ms, faster than 84.22% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 18.8 MB, less than 98.00% of Python3 online submissions for Product of Array Except Self.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_prod, prod = 1, 1
        num_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0 and num_zero == 0:
                num_zero += 1
                prod *= nums[i]
                continue
            if nums[i] == 0:
                num_zero += 1
            prod *= nums[i]
            zero_prod *= nums[i]
            
        if num_zero > 1:
            return [0 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = zero_prod
                continue
            nums[i] = prod // nums[i]
        return nums