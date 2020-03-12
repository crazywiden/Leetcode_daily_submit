"""
680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""
# two pass
# Runtime: 172 ms, faster than 53.83% of Python3 online submissions for Valid Palindrome II.
# Memory Usage: 13.2 MB, less than 68.75% of Python3 online submissions for Valid Palindrome II.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                delete_left = self.check(s[left+1:right+1])
                delete_right = self.check(s[left:right])
                if delete_left or delete_right:
                    return True
                return False
        return True
    
    def check(self, s):
        return s == s[::-1]