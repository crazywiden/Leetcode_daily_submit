"""
1392. Longest Happy Prefix
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s. Return the longest happy prefix of s .

Return an empty string if no such prefix exists.

 

Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
Example 2:

Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
Example 3:

Input: s = "leetcodeleet"
Output: "leet"
Example 4:

Input: s = "a"
Output: ""
"""
# don't understand why this is a hard
# just brutal force and passed
class Solution:
    def longestPrefix(self, s: str) -> str:
        char_idx = collections.defaultdict(list)
        n = len(s)
        all_idx = []
        for i in range(1, n):
            if s[i] == s[0]:
                all_idx.append(i)
        max_len = -1
        res = ""
        for i in range(len(all_idx)):
            latter_idx = all_idx[i]
            possible_len = n - latter_idx
            if s[latter_idx:] != s[:possible_len]:
                continue
            if possible_len > max_len:
                max_len = possible_len
                res = s[latter_idx:]
                
        return res
    