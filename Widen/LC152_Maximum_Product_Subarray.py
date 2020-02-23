"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

# similar solutiont to prefix_sum
# time complexity -- O(N)
# Runtime: 40 ms, faster than 99.91% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Maximum Product Subarray.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix_prd = 1 
        pos_min = 1 
        neg_max = 1 
        res = float("-inf")
        for num in nums:
            prefix_prd *= num 
            if prefix_prd > 0:
                res = max(res, prefix_prd / pos_min)
                pos_min = min(pos_min, prefix_prd)
            elif prefix_prd < 0:
                if neg_max == 1:
                    res = max(res, prefix_prd)
                    neg_max = prefix_prd
                else:
                    res = max(res, prefix_prd / neg_max)
                    neg_max = max(neg_max, prefix_prd)
            else:
                pos_min = 1 
                neg_max = 1 
                prefix_prd = 1 
                res = max(res, 0)
        return int(res)

# idea of dp
# https://www.cnblogs.com/grandyang/p/4028713.html
# Runtime: 52 ms, faster than 83.93% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Maximum Product Subarray.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max, curr_min = float("-inf"), float("inf")
        prev_max, prev_min = nums[0], nums[0]
        res = nums[0]
        for num in nums[1:]:
            if num > 0:
                curr_max = max(num, prev_max*num)
                curr_min = min(num, prev_min*num)
            else:
                curr_max = max(num, prev_min*num)
                curr_min = min(num, prev_max*num)
            res = max(res, curr_max)
            prev_max, prev_min = curr_max, curr_min
        return res
        