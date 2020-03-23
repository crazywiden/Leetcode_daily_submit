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

# first sort then two pointers
# time complexity -- O(N^2)
# Runtime: 2344 ms, faster than 7.20% of Python3 online submissions for 3Sum.
# Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for 3Sum.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for each element, find two sum
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            two_sum_res = self.find_two_sum(nums[i+1:], -nums[i])
            if len(two_sum_res) == 0:
                continue
            for ele in two_sum_res:
                res.append([nums[i]] + ele)
        return res
    
    def find_two_sum(self, arr, target):
        if len(arr) < 2:
            return []
        left, right = 0, len(arr)-1
        res = []
        while left < right:
            while left > 0 and left < len(arr) and arr[left-1] == arr[left]:
                left += 1
            while right < len(arr) - 1 and right >= 0 and arr[right] == arr[right+1]:
                right -= 1
            if left >= right:
                break
            if arr[left] + arr[right] == target:
                res.append([arr[left], arr[right]])
                left += 1
                right -= 1
            elif arr[left] + arr[right] < target:
                left += 1
            elif arr[left] + arr[right] > target:
                right -= 1
        return res
                
        
        

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


