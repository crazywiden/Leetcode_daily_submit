"""
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


# first idea: fix one then use 2sum
# time complexity -- O(n^2)
# TLE
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        visited = {}
        for i in range(len(nums)):
            other = self.sum_two(nums[i+1:], -nums[i])
            if len(other) == 0:
                continue
            for pair in other:
                pair += [nums[i]]
                if tuple(sorted(pair)) in visited:
                    continue
                res.append(pair)
                visited[tuple(sorted(pair))] = 0
        return res
        
    def sum_two(self, arr, target):
        search_dict = {}
        res = []
        for i in arr:
            if target-i in search_dict:
                res.append([i, target-i])
            else:
                search_dict[i] = target-i
        return res

# seems like two pointer is a must


