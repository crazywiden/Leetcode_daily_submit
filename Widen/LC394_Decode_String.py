"""
394. Decode String
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""


# stack　
# time complexity -- O(N)
# Runtime: 24 ms, faster than 94.38% of Python3 online submissions for Decode String.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Decode String.
class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 0:
            return ""
        stack = []
        idx = 0
        while idx < len(s):
            if s[idx].isnumeric():
                multiplier = []
                while s[idx].isnumeric():
                    multiplier.append(s[idx])
                    idx += 1
                stack.append("".join(multiplier))
            elif s[idx].isalpha():
                stack.append(s[idx])
                idx += 1
            elif s[idx] == "[":
                idx += 1
            elif s[idx] == "]":
                new_str = []
                while stack[-1].isalpha():
                    new_str.insert(0, stack.pop())
                multiplier = int(stack.pop())
                new_str = "".join(new_str)
                stack.append(new_str*multiplier)
                idx += 1

        return "".join(stack)