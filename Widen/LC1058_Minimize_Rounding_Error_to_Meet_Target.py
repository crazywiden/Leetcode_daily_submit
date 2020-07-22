"""

Given an array of prices [p1,p2...,pn] and a target, round each price pi to Roundi(pi) so that the rounded array [Round1(p1),Round2(p2)...,Roundn(pn)] sums to the given target. Each operation Roundi(pi) could be either Floor(pi) or Ceil(pi).

Return the string "-1" if the rounded array is impossible to sum to target. Otherwise, return the smallest rounding error, which is defined as Σ |Roundi(pi) - (pi)| for i from 1 to n, as a string with three places after the decimal.
"""



"""
Runtime: 36 ms, faster than 89.55% of Python3 online submissions for Minimize Rounding Error to Meet Target.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Minimize Rounding Error to Meet Target.
"""
import math
class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        diff_list = []
        tot_sum = 0
        UB = 0
        for ele in map(float, prices):
            diff = math.ceil(ele) - ele
            UB += math.ceil(ele)
            tot_sum += ele
            diff_list.append(diff)
        if target > UB or target < UB-len(prices):
            return "-1"
        tot_diff = abs(target - UB)
        diff_list = sorted(diff_list, reverse=True)
        tot_error = 0
        for i in range(len(diff_list)):
            if diff_list[i] == 0:
                continue
            if i < tot_diff:
                tot_error += 1-diff_list[i]
            else:
                tot_error += diff_list[i]
        if tot_error == 0 and UB != target:
            return "-1"
        
        return "{:.3f}".format(tot_error)
            