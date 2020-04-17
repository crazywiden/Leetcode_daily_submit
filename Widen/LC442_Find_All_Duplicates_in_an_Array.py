"""
442. Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

# pay great attention to the condition "1 ≤ a[i] ≤ n"
# tutorial: https://www.cnblogs.com/grandyang/p/6209746.html
# Runtime: 428 ms, faster than 17.12% of Python3 online submissions for Find All Duplicates in an Array.
# Memory Usage: 21.1 MB, less than 7.14% of Python3 online submissions for Find All Duplicates in an Array.
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                res.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        return res
    