"""
301. Remove Invalid Parentheses
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

# backtracking + validity of parentheses check
# Runtime: 120 ms, faster than 55.71% of Python3 online submissions for Remove Invalid Parentheses.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Remove Invalid Parentheses.
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        target = self.cal_remove_num(s)
        if len(target) == 0:
            return [s]
        # print(target)
        self.res = []
        self.memo = set([])
        num_remove = sum(target.values())
        self.dfs(s, num_remove, target)
        if len(self.res) == 0:
            return [""]
        return self.res
    
    def dfs(self, s, num, target):
        if s in self.memo:
            return 
        self.memo.add(s)
        if num == 0:
            if self.check_valid(s):
                self.res.append(s)
            return 
        for i in range(len(s)):
            if s[i] not in target or target[s[i]] == 0:
                continue
            new_s = s[:i] + s[i+1:]
            target[s[i]] -= 1
            self.dfs(new_s, num-1, target)      
            target[s[i]] += 1

    def check_valid(self, s):
        if len(s) == 0:
            return True
        stack = []
        for i in range(len(s)):
            if s[i] == ")":
                if len(stack) == 0:
                    return False
                if stack[-1] != "(":
                    return False
                stack.pop()
            elif s[i] == "(":
                stack.append(s[i])
        return True
    
    def cal_remove_num(self, s):
        target = {"(":0, ")":0}
        stack = []
        for i in range(len(s)):
            if s[i] == ")":
                if len(stack) == 0:
                    target[s[i]] += 1
                elif stack[-1] != "(":
                    target[s[i]] += 1
                elif stack[-1] == "(":
                    stack.pop()
            elif s[i] == "(":
                stack.append(s[i])
        for i in range(len(stack)):
            if stack[i] == "(":
                target["("] += 1
        return {key:val for key, val in target.items() if val != 0}
    
    
    