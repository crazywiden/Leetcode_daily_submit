"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

# back tracking
# Runtime: 40 ms, faster than 26.72% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Generate Parentheses.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        target = {"left":n, "right":n}
        curr = {"left":0, "right":0}
        res = set([])
        self.dfs(res, [], target, curr)
        return res
    
    def dfs(self, res, tmp, target, current):
        # print("target:", target, "current:", current)
        # print("tmp:", tmp)
        
        if target["left"] < 0 or target["right"] < 0:
            return 
        
        if target["left"] == 0 and target["right"] == 0:
            res.add("".join(tmp))
            return 

        target["left"] -= 1
        current["left"] += 1
        tmp.append("(")
        self.dfs(res, tmp, target, current)
        target["left"] += 1
        current["left"] -= 1
        tmp.pop()

        if current["left"] < current["right"] + 1:
            return 
        target["right"] -= 1
        current["right"] += 1
        tmp.append(")")
        self.dfs(res, tmp, target, current)
        target["right"] += 1
        current["right"] -= 1
        tmp.pop()

            
                
        