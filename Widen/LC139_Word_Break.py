"""
139. Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""



# dfs -- ETL
# time complexity -- O(N^2)
# most time spend in comparasion between word in wordDict and subarray of s
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(wordDict) == 0:
            return False
        
        self.word_len = defaultdict(list)
        for word in wordDict:
            self.word_len[len(word)].append(word)
        sorted_len = sorted(list(self.word_len.keys()))
        if len(s) < sorted_len[0]:
            return False
        return self.helper(sorted_len, s)
        
    def helper(self, sorted_len, s):
        if len(s) == 0:
            return True
        
        if len(s) < sorted_len[0]:
            return False
        flag = False
        for key in sorted_len:
            for word in self.word_len[key]:
                if word == s[:key]:
                    flag = self.helper(sorted_len, s[key:])
                if flag:
                    return True
        return False



# dp
# time complexity -- O(N^2)
# can save the result of string comparasion
# Runtime: 40 ms, faster than 81.07% of Python3 online submissions for Word Break.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Word Break.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(wordDict) == 0:
            return False
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]
                
        



