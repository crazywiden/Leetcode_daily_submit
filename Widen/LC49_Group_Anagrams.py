"""
49. Group Anagrams
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        res_dict = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            res_dict[sorted_word].append(word)
        return [val for key, val in res_dict.items()]
        