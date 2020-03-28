"""
809. Expressive Words
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 

Notes:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
"""

# running length
# collections.Counter() does work in this problem
# whenever do Counter(), rethink does order matters
# Runtime: 48 ms, faster than 77.72% of Python3 online submissions for Expressive Words.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Expressive Words.
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        base_char, base_freq = self.get_freq(S)
        res = 0
        for word in words:
            word_char, word_freq = self.get_freq(word)
            if word_char != base_char:
                continue
            is_done = True
            for base_val, word_val in zip(base_freq, word_freq):
                if base_val == word_val:
                    continue
                if base_val < word_val:
                    is_done = False
                    break
                if base_val < 3 and base_val != word_val:
                    is_done = False
                    break
            if is_done:
                res += 1
        return res
    
    def get_freq(self, s):
        char = ""
        prev_s = s[0]
        freq = []
        idx = 0
        cnt = 0
        while idx < len(s):
            if prev_s == s[idx]:
                cnt += 1
                idx += 1
                continue
            char += s[idx]
            prev_s = s[idx]
            freq.append(cnt)
            idx += 1
            cnt = 1
        if cnt != 0:
            char += s[idx-1]
            freq.append(cnt)
        return char, freq
    
    
    