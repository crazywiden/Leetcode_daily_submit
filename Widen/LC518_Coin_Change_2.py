"""
LC518 Coin Change

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""

# official solution
# link: https://leetcode.com/articles/coin-change-ii/
# Runtime: 128 ms, faster than 97.56% of Python3 online submissions for Coin Change 2.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Coin Change 2.
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]



# backpack problem
# dp -- be extremly careful that we don't need to check 
# whether coins[i-1] is larger than current amount or not
# k did this
# but obviously this can be improved using rolling array
# time complexity -- O(n^2 * amount)
# memory complexity -- O(n* amount)
# Runtime: 8856 ms, faster than 5.02% of Python3 online submissions for Coin Change 2.
# Memory Usage: 33.9 MB, less than 16.67% of Python3 online submissions for Coin Change 2.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(n+1)] for _ in range(amount+1)]
        for i in range(n+1):
            dp[0][i] = 1
            
        for i in range(1, amount+1):
            for j in range(1, n+1):
                k = i // coins[j-1]
                for t in range(k+1):
                    dp[i][j] += dp[i-t*coins[j-1]][j-1]
        return dp[-1][-1]
    

# memeory optimization using rolling array
# time complexity -- O(n^2 * amount)
# memory complexity -- O(n)
# Runtime: 484 ms, faster than 24.74% of Python3 online submissions for Coin Change 2.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Coin Change 2.


class Solution:
    def change(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(target+1)] for _ in range(2)]
        new, old = 0, 1 
        dp[0][0] = 1  
        for i in range(1, n+1):
            new, old = 1-new, new
            dp[new][0] = 1
            for j in range(1, target + 1):
                dp[new][j] = dp[old][j]
                if j >= nums[i-1]:
                    dp[new][j] += dp[new][j-nums[i-1]]
        return dp[new][-1]
    
# don't know what's wrong with this code...
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(2)]
        new, old = 0, 1
        dp[new][0] = 1
        for index in range(1, n+1):
            old = new
            new = 1 - new
            # dp[new][0] = 1
            for val in range(amount+1):
                if val == 0:
                    dp[new][val] = 1
                    continue
                dp[new][val] = dp[old][val]
                if val >= coins[index-1]:
                    dp[new][index] += dp[new][val-coins[index-1]]
                # k = val // coins[index-1]
                # for mult in range(k+1):
                #     dp[new][val] += dp[old][val-mult*coins[index-1]]
        return dp[new][-1]
    
    
                
                



