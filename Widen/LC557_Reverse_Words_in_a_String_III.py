
"""
LC557. Reverse Words in a String III
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""



# very easy a problem
# Runtime: 20 ms, faster than 85.33% of Python online submissions for Reverse Words in a String III.
# Memory Usage: 13.1 MB, less than 45.45% of Python online submissions for Reverse Words in a String III.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        if s[-1] == " ":
            s = s[:-1]
        return " ".join([i[::-1] for i in s.split(" ")])
        