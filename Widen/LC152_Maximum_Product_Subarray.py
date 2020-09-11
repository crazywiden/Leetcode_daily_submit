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


# i was so great before...
# prefix sum to solve in O(N)
# Runtime: 56 ms, faster than 77.80% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 14.8 MB, less than 18.07% of Python3 online submissions for Maximum Product Subarray.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = float("-inf")
        idx = 0
        tmp = []
        is_met_zero = False
        while idx < len(nums):
            if nums[idx] == 0:
                is_met_zero = True
                max_prod = max(max_prod, 0)
                curr_max_prod = self.cal_max_prod(tmp)
                max_prod = max(max_prod, curr_max_prod)
                tmp = []
            else:
                tmp.append(nums[idx])
            idx += 1
        if is_met_zero:
            return max(max_prod, self.cal_max_prod(tmp))
        max_prod = self.cal_max_prod(nums)
        return max_prod
    
    def cal_max_prod(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        prefix_prd = [1 for _ in range(n+1)]
        for i in range(1, n+1):
            prefix_prd[i] = prefix_prd[i-1] * nums[i-1]
        res = float("-inf")
        max_neg = float("-inf")
        for i in range(1, n+1):
            if prefix_prd[i] > 0:
                res = max(res, prefix_prd[i])
            else:
                if max_neg != float("-inf"):
                    res = max(res, prefix_prd[i]/max_neg)
                else:
                    res = max(res, prefix_prd[i])
                max_neg = max(prefix_prd[i], max_neg)
        return res
# similar solution to prefix_sum
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
        