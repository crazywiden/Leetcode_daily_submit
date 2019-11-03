"""
LC53 Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

# actually a very very simple but annoying problem...
# which shows my weakness in writing bug-free code
# Runtime: 76 ms, faster than 79.49% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.6 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # first jump all negative values at the beginning
        start = 0
        for i in range(n):
            if nums[i] <= 0:
                continue
            else:
                sub_sum, tot_sum = nums[i], nums[i]
                start = i
                break
        if start == 0 and max(nums) <= 0:
            return max(nums)


        for i in range(start+1, n):
            if sub_sum <= 0 and nums[i] < 0:
                sub_sum = max(sub_sum, nums[i])
                continue
            if nums[i] <= 0:
                tot_sum = max(tot_sum, sub_sum)
            sub_sum += nums[i]
            if sub_sum <= 0:
                sub_sum = 0
                continue
            # print(tot_sum, sub_sum, nums[i])
        return max(tot_sum, sub_sum)


# a very neat solution
# Runtime: 68 ms, faster than 98.47% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.6 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, sub_sum = nums[0], nums[0]
        for num in nums[1:]:
            s = num
            if sub_sum > 0:
                s += sub_sum
            max_sum = max(s, max_sum)
            sub_sum = s
        return max_sum
