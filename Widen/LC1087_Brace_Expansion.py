"""
LC 1087 -- Brace Expansion

A string S represents a list of words.

Each letter in the word has 1 or more options.  
If there is one option, the letter is represented as is.  
If there is more than one option, then curly braces delimit the options.  
For example, "{a,b,c}" represents options ["a", "b", "c"].
For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].
Return all words that can be formed in this manner, in lexicographical order.
Example 1:
Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]

Example 2:
Input: "abcd"
Output: ["abcd"]
"""


# why is this backtracking?
# Runtime: 48 ms, faster than 54.12% of Python3 online submissions for Brace Expansion.
# Memory Usage: 14 MB, less than 25.00% of Python3 online submissions for Brace Expansion.
class Solution:
    def expand(self, S: str):
        if len(S) == 0:
            return []
        
        def helper(sub_str, start):
            if len(sub_str) == 0:
                return ""
            res = [""]
            while start < len(sub_str):
                if sub_str[start]  == "}":
                    start += 1
                    continue

                if sub_str[start] == "{":
                    start = start + 1
                    tmp = []
                    while sub_str[start] != "}":
                        if sub_str[start] != ",":
                            tmp.append(sub_str[start])
                        start += 1
                    new_res = []
                    for i in range(len(res)):
                        for j in range(len(tmp)):
                            new_res.append(res[i] + tmp[j])

                    res = new_res.copy()
                    del new_res
                else:
                    for i in range(len(res)):
                        res[i] += sub_str[start]
                    start += 1
            return res

        return helper(S, 0)
