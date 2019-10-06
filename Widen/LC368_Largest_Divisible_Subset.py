"""
Given a set of distinct positive integers, 
find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""
# method 1 -- dfs 
# TLE at 31/41
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        def dfs(nums, res_list, start):
            if start >= len(nums)-1:
                return res_list
            longest_part = []
            cnt = 0
            for i in range(start+1, len(nums)):
                if nums[i] % res_list[-1] == 0:
                    res_list.append(nums[i])
                    part_list = dfs(nums, res_list, i)
                    if len(part_list) > cnt:
                        cnt = len(part_list)
                        longest_part = part_list.copy()
                    res_list.pop()
            if len(longest_part) == 0:
                return res_list
            else:
                return longest_part
        
        cnt = 0
        longest_res = []
        nums = sorted(nums)
        search_history = set()
        for i in range(len(nums)):
            if i in search_history:
                continue
            tmp_res = dfs(nums, [nums[i]], i)
            if len(tmp_res) > cnt:
                longest_res = tmp_res.copy()
                cnt = len(tmp_res)
            search_history.update(tmp_res)
        return longest_res


# method 2 -- reference: https://blog.csdn.net/fuxuemingzhu/article/details/83027364
# Runtime: 448 ms, faster than 22.02% of Python3 online submissions for Largest Divisible Subset.
# Memory Usage: 13.9 MB, less than 20.00% of Python3 online submissions for Largest Divisible Subset.
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: 
            return []
        N = len(nums)
        nums.sort()
        dp = [0] * N # LDS
        parent = [0] * N
        mx = 0
        mx_index = -1
        for i in range(N):
            for j in range(i - 1, -1 , -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > mx:
                        mx = dp[i]
                        mx_index = i
        res = list()
        for k in range(mx + 1):
            res.append(nums[mx_index])
            mx_index = parent[mx_index]
        return res[::-1]