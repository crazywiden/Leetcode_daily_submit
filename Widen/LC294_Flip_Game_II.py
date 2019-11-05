"""
LC294 Flip Game II
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:

Input: s = "++++"
Output: true 
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
"""

# dfs with memory
# time complexity -- O(N**2)
# Runtime: 156 ms, faster than 38.78% of Python3 online submissions for Flip Game II.
# Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Flip Game II.
class Solution:
    def canWin(self, s: str) -> bool:
        memo = {}
        def helper(sub_s):
            if sub_s in memo:
                return memo[sub_s]

            is_win = False
            for i in range(2, len(sub_s)+1):
                if sub_s[i-2:i] == "++":
                    new_s = sub_s[:max(0,i-2)] + "--" + sub_s[i:]
                    memo[new_s] = helper(new_s)
                    if not memo[new_s]:
                        is_win = True
            return is_win
        return helper(s)


# method2 -- dp
# used better pruning method
class Solution:
    def canWin(self, s: str) -> bool:
        memo = {}
        def helper(piles):
            piles = tuple(sorted([p for p in piles if p>=2]))
            if not piles:
                return False
            if piles in memo:
                return memo[piles]
            for i, pile in enumerate(piles):
                for j in range(pile-1):
                    result = helper(piles[:i] + (j, pile-j-2)+ piles[i+1:])
                    if not result:
                        memo[piles] = True
                        return True
            memo[piles] = False
            return False
        pieces = s.split('-')
        piles = tuple([len(x) for x in pieces if len(x)>1])
        return helper(piles)  


a = (1, 3)
b = (3,43)
print(a + b)



                