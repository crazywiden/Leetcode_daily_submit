"""
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


# two pointer
# time complexity -- O(N)
# Runtime: 68 ms, faster than 62.27% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        repeat = set([])
        repeat.add(s[0])
        left, right = 0, 1
        res = -1
        while right < len(s):
            if s[right] in repeat:
                res = max(res, right-left)
                repeat.remove(s[right])
                while s[left] != s[right]:
                    repeat.remove(s[left])
                    left += 1
                left += 1
            else:
                repeat.add(s[right])
                right += 1
        res = max(res, right-left)
        return res
            
        