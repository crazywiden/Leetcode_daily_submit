"""
151. Reverse Words in a String
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""


# very simple implementation again
# Runtime: 20 ms, faster than 64.28% of Python online submissions for Reverse Words in a String.
# Memory Usage: 13 MB, less than 78.05% of Python online submissions for Reverse Words in a String.
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = [i for i in s.split(" ") if len(i) != 0]
        return " ".join(tmp[::-1])