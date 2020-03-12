"""
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""

# similar to rolling hash method
# time complexity -- O(len(s)+len(p))
# Runtime: 248 ms, faster than 18.24% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Find All Anagrams in a String.
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = collections.Counter(p)
        n_s, n_p = len(s), len(p)
        if n_s < n_p:
            return []
        res = []
        candidate = collections.Counter(s[:n_p])
        if self.check_same(candidate, target):
            res.append(0)
        for i in range(1, n_s-n_p+1):
            candidate[s[i-1]] -= 1
            if s[i+n_p-1] in candidate:
                candidate[s[i+n_p-1]] += 1
            else:
                candidate[s[i+n_p-1]] = 1
            if self.check_same(target, candidate):  # this is O(1) because we only have 26 characters
                res.append(i)
        return res
    
    def check_same(self, dict1, dict2):
        for key, val in dict1.items():
            if key not in dict2:
                return False
            if val != dict2[key]:
                return False
        return True
    