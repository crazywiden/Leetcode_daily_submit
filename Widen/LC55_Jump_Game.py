"""
55. Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

# brilliant solution! no dp, just greedy
# same with the lc 45 jump game II
# dp will TLE but greedy will win
# time complexity -- O(N)
# Runtime: 88 ms, faster than 82.43% of Python3 online submissions for Jump Game.
# Memory Usage: 14.9 MB, less than 7.14% of Python3 online submissions for Jump Game.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for idx, num in enumerate(nums):
            if max_reach < idx:
                return False
            max_reach = max(max_reach, num+idx)
        return True
    