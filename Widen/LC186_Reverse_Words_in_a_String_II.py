"""

LC 186. Reverse Words in a String II


Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""




# easy, a little tricky is the problem is need to be done in-place
# Runtime: 232 ms, faster than 78.48% of Python online submissions for Reverse Words in a String II.
# Memory Usage: 20.7 MB, less than 100.00% of Python online submissions for Reverse Words in a String II.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        s.reverse()
        left = 0
        right = 0
        while right < len(s):
            if s[right] == " ":
                if left == 0:
                    s[left:right] = s[right-1::-1]
                else:
                    s[left+1:right] = s[right-1:left:-1]
                left = right
                # break
            right += 1

        if left != 0:
            if s[-1] != " ":
                s[left+1:] = s[right-1:left:-1]
        else:
            s.reverse()
