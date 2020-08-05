"""
LC300 --  Longest Increasing Subsequence
Description:

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

# dp
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        N = len(nums)
        dp = [1 for _ in range(N)]
        for i in range(1, N):
            for j in range(i-1, -1, -1):
                if nums[j] >= nums[i]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
# credit to -->  https://www.cnblogs.com/grandyang/p/4938187.html

# solutoin 1 -- dp
# time complexity -- O(N^2)
# space complexity -- O(N)
# Runtime: 1120 ms, faster than 33.91% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14 MB, less than 5.13% of Python3 online submissions for Longest Increasing Subsequence.
# dp[i] means the length of increasing subarray ends with nums[i]
# transfer formula: dp[i] = max(dp[i], dp[j] + 1) for j < i and nums[j] < nums[i]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [1 for _ in range(n)]
        res = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(dp[i], res)
        return res

# solutoin 2 -- maintain a list of sorted value, use binary search(similar to np.searchsorted()) to speed up
# time complexity -- O(nlog(n))
# space complexity -- O(N)
# Runtime: 48 ms, faster than 90.47% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 13.9 MB, less than 5.13% of Python3 online submissions for Longest Increasing Subsequence.
# brilliant move:
# maintain a list: records (initialized by records[0] = nums[0])
# if nums[i] < records[0], replace records[0] with nums[i]
# if nums[i] > records[-1], append nums[i] at the back of records[-1]
# else replace records[j] with nums[i] to maintain order in records
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(arr, left, right, val):
            if left >= right:
                return right
            mid = int((left + right)/2)
            if arr[mid] < val:
                return binary_search(arr, mid+1, right, val)
            elif arr[mid] > val:
                return binary_search(arr, left, mid-1, val)
            else:
                return mid
            
        if len(nums) == 0:
            return 0
        records = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > records[-1]:
                records.append(nums[i])
            elif nums[i] <= records[0]:
                records[0] = nums[i]
            else:
                idx = binary_search(records, 0, len(records)-1, nums[i])
                if nums[i] > records[idx]:
                    records[idx+1] = nums[i]
                else:
                    records[idx] = nums[i]
        return len(records)
