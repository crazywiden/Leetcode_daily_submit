"""
363. Max Sum of Rectangle No Larger Than K
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
Note:

The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
"""


# essentially two problems:
# 1. find the maximum rectangle area in a matrix
# 2. find the maximum continuous sum of subarray that smaller than k
# time complexity -- O(n_col*n_col*n_row*log(n_row))
# Runtime: 1012 ms, faster than 50.80% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
# Memory Usage: 13.7 MB, less than 75.00% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.

import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n_row, n_col = len(matrix), len(matrix[0])
        overall_max = float("-inf")
        for left in range(n_col):
            row_sum = [0 for _ in range(n_row)]
            for right in range(left, n_col):
                for i in range(n_row):
                    row_sum[i] += matrix[i][right]
                curr_max = self.find_subarray_smaller_than_k(row_sum, k)
                overall_max = max(overall_max, curr_max)
        return overall_max
    
    def find_subarray_smaller_than_k(self, arr, k):
        # arr is unsorted array
        max_sum = float("-inf")
        diff_arr = [0]
        cumsum_arr = 0
        for i in range(len(arr)):
            cumsum_arr += arr[i]
            tmp_diff = cumsum_arr - k
            idx = bisect.bisect_left(diff_arr, tmp_diff)
            if idx != len(diff_arr): # there is an sub-array with sum less than k
                max_sum = max(max_sum, cumsum_arr-diff_arr[idx])
            bisect.insort_left(diff_arr, cumsum_arr)
        return max_sum






