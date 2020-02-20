"""
LC76 Minimum window subarray
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


# Runtime: 228 ms, faster than 21.13% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 13.4 MB, less than 61.11% of Python3 online submissions for Minimum Window Substring.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n_s, n_t = len(s), len(t)
        if n_s < n_t:
            return ""
        # two pointers
        res = ""
        min_len = n_s + 1
        left, right = 0, 0
        tot_num = 0
        freq = {c:0 for c in t}
        raw = collections.Counter(t)
        stack = [] # each element is a index 
        
        while right < n_s:
            if s[right] not in t:
                right += 1
                continue
            # update freq
            freq[s[right]] += 1
            if freq[s[right]] == raw[s[right]]:
                tot_num += 1
            stack.append(right)
            while tot_num == len(raw):
                left = stack.pop(0)
                if right-left+1 < min_len:
                    min_len = right-left+1
                    res = s[left:right+1]
                freq[s[left]] -= 1
                if freq[s[left]] < raw[s[left]]:
                    tot_num -= 1
            right += 1 
        return res
                
            
            