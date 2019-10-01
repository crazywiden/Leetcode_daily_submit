"""
LC322 --  Coin Change
time complexity -- O(N*M)
space complexiy -- O(M)
M is len(coins), N is amount
Runtime: 1080 ms, faster than 85.13% of Python3 online submissions for Coin Change.
Memory Usage: 13.8 MB, less than 30.56% of Python3 online submissions for Coin Change.
normal dp
small trick is to build a n+1 length dp array
however, still pretty slow if no optimization is used
"""
# method1 -- no optimization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        dp = [amount + 1] * (amount + 1)
        for i in range(amount + 1):
            if i in coins:
                dp[i] = 1
                continue
            candidates = [dp[i - coin] + 1 for coin in coins if i - coin > 0]
            if candidates:
                dp[i] = min(candidates)

        return -1 if dp[amount] > amount else dp[amount]

# method2 -- dfs, first sort the coins array
# this dfs is also smart
# should think more about his pruning trick
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        MAX = amount + 1
        self.ans = MAX
        def dfs(coin_idx, tot_num, amount):
            if amount == 0:
                self.ans = tot_num
                return
            if coin_idx == len(coins):
                return 
            coin = coins[coin_idx]
            for k in range(amount//coin, -1, -1):
                if tot_num + k >= self.ans:
                    break
                dfs(coin_idx+1, tot_num+k, amount-k*coin)
        dfs(0, 0, amount)
        return -1 if self.ans==MAX else self.ans
