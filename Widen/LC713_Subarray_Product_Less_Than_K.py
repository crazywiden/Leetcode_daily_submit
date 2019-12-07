"""
713. Subarray Product Less Than K
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

"""

# two pointer -- sliding window
# time complexity -- O(N)
# even know the solution, should be careful about the corner cases...
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        left, right = 0, 0
        sub_prod = 1
        res = 0
        while left <= right and right < len(nums):
            sub_prod *= nums[right]
            while sub_prod >= k:
                sub_prod /= nums[left]
                left += 1
                if left >= len(nums):
                    return res 
            res += right - left + 1
            right += 1
        return res


