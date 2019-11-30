"""
140. Word Break II
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

# dp 
# want to do similar things as LC139, TLE...
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if len(wordDict) == 0:
            return []
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        break_word = {i:[] for i in range(len(s)+1)}
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    if len(break_word[j]) == 0:
                        break_word[i].append([s[j:i]])
                    else:
                        for seq in break_word[j]:
                            new_seq = seq.copy()
                            new_seq.append(s[j:i])
                            break_word[i].append(new_seq)
        res = []
        for seq in break_word[len(s)]:
            res.append(" ".join(seq))
        return res
        
# try dfs?
# time complexity -- O(N^2)
# use of memory is very smart
# didn't use index as key, use sub-string as key, so when there are a lot of duplicates in the original string
# it will be more faster
# Runtime: 48 ms, faster than 79.16% of Python3 online submissions for Word Break II.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Word Break II.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if len(wordDict) == 0:
            return []
        res = []
        self.memo = {}
        return self.dfs(s, wordDict, [])
        
    def dfs(self, s, wordDict, res):
        if s in self.memo:
            return self.memo[s]
        if len(s) == 0:
            return [""]
        res = []
        for word in wordDict:
            if s[:len(word)] == word:
                for seg in self.dfs(s[len(word):], wordDict, res):
                    res.append(word + ("" if not seg else " " + seg))
        self.memo[s] = res
        return res








