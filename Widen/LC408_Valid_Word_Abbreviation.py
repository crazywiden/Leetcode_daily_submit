"""
408. Valid Word Abbreviation
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:
Given s = "apple", abbr = "a2e":

Return false.
"""


# easy question is always very annoying...
# Runtime: 28 ms, faster than 98.80% of Python3 online submissions for Valid Word Abbreviation.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Valid Word Abbreviation.
import re
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr_char = re.findall("[a-z]+", abbr)
        abbr_digit = re.findall("[0-9]+", abbr)
        if abbr[0] >= "0" and abbr[0] <= "9":
            if int(abbr_digit[0]) > len(word):
                return False
            if abbr[0][0] == "0":
                return False
            return self.compare(word[int(abbr_digit[0]):], abbr_char, abbr_digit[1:])
        else:
            return self.compare(word, abbr_char, abbr_digit)

    def compare(self, word, abbr_char, abbr_digit):
        start = 0
        if len(abbr_char) == 0 and len(word) != 0:
            return False
        while start < len(word):
            if len(abbr_char) != 0:
                tmp_seg = abbr_char.pop(0)
                if word[start:start+len(tmp_seg)] != tmp_seg:
                    return False
                start = start + len(tmp_seg)
            if len(abbr_digit) != 0:
                tmp_abbr = abbr_digit.pop(0)
                if tmp_abbr[0] == "0":
                    return False
                start += int(tmp_abbr)
            if len(abbr_char) == 0 and len(abbr_digit) == 0:
                break
        if len(abbr_char) == 0 and len(abbr_digit) == 0 and start == len(word):
            return True
        else:
            return False




