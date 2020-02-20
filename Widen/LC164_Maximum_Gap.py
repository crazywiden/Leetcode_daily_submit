"""
164. Maximum Gap
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
"""

# the idea of bucket is soooo brilliant! 
# time complexity -- O(N)
# but it's clear that using Python.sort() will be faster LOL
# so python built-in function is really optimized 
# also namedtuple can't change value is a little bit annoying
# Runtime: 128 ms, faster than 6.43% of Python3 online submissions for Maximum Gap.
# Memory Usage: 14.6 MB, less than 33.33% of Python3 online submissions for Maximum Gap.
from collections import namedtuple
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        nums_max, nums_min = max(nums), min(nums)
        if nums_max == nums_min:
            return 0
        Bucket = namedtuple("Bucket", ["is_used", "min_val", "max_val"])
        bucket_size = max(1, (nums_max - nums_min) // (n-1))
        bucket_num = (nums_max-nums_min)//bucket_size + 1
        bucket_list = [Bucket(False, float("inf"), float("-inf")) for _ in range(bucket_num)]
        for num in nums:
            idx = (num - nums_min) // bucket_size
            bucket_list[idx] = bucket_list[idx]._replace(is_used=True)
            bucket_list[idx] = bucket_list[idx]._replace(min_val=min(num, bucket_list[idx].min_val))
            bucket_list[idx] = bucket_list[idx]._replace(max_val=max(num, bucket_list[idx].max_val))
            
        res = 0
        prev_max = nums_min
        for i in range(bucket_num):
            if not bucket_list[i].is_used:
                continue
            res = max(res, bucket_list[i].min_val - prev_max)
            prev_max = bucket_list[i].max_val
            
        return res
        