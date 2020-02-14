"""
410. Split Array Largest Sum
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""



# every time do a problem, try to finish it in a clearer mind

# think of dp first but not completed 
# this interval dp method is stolen from the internet
# time complexity -- O(n^2 * m)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if m == 1:
            return sum(nums)
        n = len(nums)
        prefix_sum = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            prefix_sum[i] = nums[i-1] + prefix_sum[i-1]
        
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][1] = prefix_sum[i]
        
        for i in range(1, n+1):
            for j in range(2, min(i, m)+1): # how many subarrays
                tmp = float("inf")
                for k in range(1, i-j+2):
                    tmp = min(tmp, max(dp[i-k][j-1], prefix_sum[i]-prefix_sum[i-k]))
                dp[i][j] = tmp
                
        return dp[-1][-1]
        


# binary search of answer
# so brilliant!
# key part: determine the upper bound and lower bound of the searching space
# key part2: find out how to check validility
# look at this explanation:leetcode.com/articles/split-array-largest-sum/127692/Split-Array-Largest-Sum/327562
# Runtime: 32 ms, faster than 78.93% of Python3 online submissions for Split Array Largest Sum.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Split Array Largest Sum.

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = left + (right-left) // 2
            if self.valid(nums, mid, m):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    
    def valid(self, nums, val, k):
        cnt = 0
        cum_sum = 0
        for num in nums:
            cum_sum += num
            if cum_sum > val:
                cnt += 1 
                if cnt >= k:
                    return False
                cum_sum = num
        return True



