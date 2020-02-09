"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""


# Runtime: 28 ms, faster than 68.02% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 12.9 MB, less than 98.53% of Python3 online submissions for Letter Combinations of a Phone Number.
KEYBOARD = {
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        self.dfs(res, [], digits)
        return ["".join(i) for i in res]
        
    
    def dfs(self, res, tmp, digits):
        if len(digits) == 0:
            res.append(tmp.copy())
            return 
        
        for l in KEYBOARD[digits[0]]:
            tmp.append(l)
            self.dfs(res, tmp, digits[1:])
            tmp.pop()
        