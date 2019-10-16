"""
LC740  Delete and Earn
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
 

Example 2:

Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
"""


# a variantion of House Rubber
# use dp in separate segement to solve
# time complexity -- O(N^2)
# space complexity -- O(N)
# Runtime: 68 ms, faster than 64.57% of Python3 online submissions for Delete and Earn.
# Memory Usage: 14 MB, less than 25.00% of Python3 online submissions for Delete and Earn.
# this code is not very concise
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = nums[i]
            else:
                freq[nums[i]] += nums[i]
        res = 0
        continuous_num = []
        for key in sorted(freq.keys()):
            if (key-1 not in freq) and (key + 1) not in freq:
                res += freq[key]  # delete this key   
            elif (key-1 in freq) and (key+1 in freq):
                new_key[key] = freq[key]
            elif key-1 in freq:
                new_key[key] = freq[key]
                continuous_num.append(new_key)
                new_key = {}
            elif key+1 in freq:
                new_key = {}
                new_key[key] = freq[key]
        
        for seq in continuous_num:
            res += self.helper(seq)
        return res
                
    def helper(self, seq):
        result = [seq[key] for key in sorted(seq.keys())]
        if len(result) == 2:
            return max(result)
        dp = [0 for _ in range(len(result))]
        dp[0], dp[1] = result[0], result[1]
        dp[2] = result[2] + dp[0]
        for i in range(3, len(result)):
            dp[i] = result[i] + max(dp[i-2], dp[i-3])
        return max(dp[-1], dp[-2])
        
# method 2:
from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        prev = 0
        prevprev = 0
        counter = Counter(nums)
        keys = sorted(counter.keys())
        for num in keys:
            if num-1 in counter:
                curr = max(prevprev+num*counter[num],prev)
                prevprev,prev = prev,curr
            else:
                prevprev,prev = prev,prev+num*counter[num]
        return prev
            
            
            
        
        