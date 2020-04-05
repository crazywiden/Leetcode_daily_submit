"""
697. Degree of an Array
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        ele_idx = collections.defaultdict(list)
        for idx, ele in enumerate(nums):
            ele_idx[ele].append(idx)
        max_freq = -1
        min_len = len(nums) + 1
        for key, l in ele_idx.items():
            if len(l) > max_freq:
                max_freq = len(l)
                min_len = l[-1]-l[0] + 1
            elif len(l) == max_freq:
                min_len = min(min_len, l[-1]-l[0] + 1)
        return min_len
    
    
    