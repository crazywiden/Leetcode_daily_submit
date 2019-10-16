"""
LC 486 -- predict the winner
Given an array of scores that are non-negative integers. 
Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. 
Each time a player picks a number, that number will not be available for the next player. 
This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. 
You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.
Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. 
	No matter which number player 2 choose, player 1 can choose 233.
	Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
"""

# first solution: 
# reference: https://blog.csdn.net/cloudox_/article/details/64122204
# soooo simple and elegant
# time complexity -- O(2^N)
# space complexity -- O(N)
# TLE however...
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(nums, start, end):
            if start == end:
                return nums[start]
            first = nums[start] - helper(nums, start+1, end)
            last = nums[end] - helper(nums, start, end-1)
            return max(first, last)
        ans_diff = helper(nums, 0, len(nums)-1)
        return ans_diff >= 0


# second solution: based on strategy
# after I select a number, the other one must will select a number that will left minimum number to me
# also TLE...
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right):
            if left == right:
                return nums[left]
            if left > right:
                return 0
            left_score = nums[left] + min(helper(left+1, right-1), helper(left+2, right))
            right_score = nums[right] + min(helper(left+1, right-1), helper(left, right-2))
            return max(left_score, right_score)
        final_score = helper(0, len(nums)-1)
        return final_score*2 >= sum(nums)



# third solution: add memorization
# Runtime: 44 ms, faster than 43.56% of Python3 online submissions for Predict the Winner. 
# Memory Usage: 14 MB, less than 20.00% of Python3 online submissions for Predict the Winner.
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right):
            if left == right:
                return nums[left]
            if left > right:
                return 0
            if dp[left][right] != -1:
                return dp[left][right]
            
            left_score = nums[left] + min(helper(left+1, right-1), helper(left+2, right))
            right_score = nums[right] + min(helper(left+1, right-1), helper(left, right-2))
            dp[left][right] = max(left_score, right_score)
            return dp[left][right]
        dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
        final_score = helper(0, len(nums)-1)
        return final_score*2 >= sum(nums)


# so brilliant idea!!
# https://leetcode.com/problems/predict-the-winner/discuss/96832/c-dp-solution-with-explanation
# need a lot of math derivation... definitely can't think of in a short time period






