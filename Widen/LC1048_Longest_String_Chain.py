"""
1048. Longest String Chain

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
"""
# dp: dp[i] is the longest length of the word chain dp[i] = max(dp[i], dp[j]+1) if two words are in a chain
# note that we should first sort the word list by word length
# time complexity -- O(N^2 * max(len(word)))
# Runtime: 1760 ms, faster than 12.68% of Python3 online submissions for Longest String Chain.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Longest String Chain.
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words = sorted(words, key=lambda x:len(x))
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if self.is_precessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    def is_precessor(self, word1, word2):
        if len(word1) != len(word2) - 1:
            return False
        p1, p2 = 0, 0
        is_inserted = False
        while p1<len(word1) and p2 < len(word2):
            if word1[p1] != word2[p2]:
                if is_inserted:
                    return False
                is_inserted = True
                p2 += 1
                continue
            p1 += 1
            p2 += 1
        return True
    