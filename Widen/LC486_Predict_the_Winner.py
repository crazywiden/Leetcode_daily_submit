"""
486. Predict the Winner
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

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
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
"""

# dp with memorty
# very important to design status and memory!!
# time complexity -- O(n^2)
# much more faster than mini-max
# Runtime: 28 ms, faster than 97.64% of Python3 online submissions for Predict the Winner.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Predict the Winner.
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[None for _ in range(len(nums))] for _ in range(len(nums))]
        final_score = self.helper(nums, 0, len(nums)-1, dp)
        return final_score >= 0
    def helper(self, nums, left, right, dp):
        if left == right:
            return nums[left]
        if dp[left][right] is not None:
            return dp[left][right]
        take_left = nums[left] - self.helper(nums, left+1, right, dp)
        take_right = nums[right] - self.helper(nums, left, right-1, dp)
        dp[left][right] = max(take_left, take_right)
        return dp[left][right]