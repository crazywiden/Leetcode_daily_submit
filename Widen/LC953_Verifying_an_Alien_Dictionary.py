"""
953. Verifying an Alien Dictionary
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
"""

# my solution
# pretty intuitive and greedy
# basic idea: compare each words first element, second element...
# Runtime: 32 ms, faster than 78.00% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Verifying an Alien Dictionary.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_idx = {c:idx for idx, c in enumerate(order)}
        char_idx[""] = -1
        n = len(words)
        stack = [-1]
        is_done = False
        # prev_equal[i] == True means words[i][0] == words[i-1][0]
        prev_equal = [True for _ in range(n)]
        prev_equal[0] = False
        while not is_done:
            for i in range(n):
                # print(words)
                if len(words[i]) == 0:
                    if not prev_equal[i]:
                        stack.append(-1)
                        continue
                    return False
                idx = char_idx[words[i][0]]
                words[i] = words[i][1:]
                if idx < stack[-1]:
                    if prev_equal[i] == False:
                        stack.append(idx)
                        continue
                    return False
                if idx == stack[-1]:
                    prev_equal[i] = True
                else:
                    prev_equal[i] = False
                stack.append(idx)
            stack = [-1]
            is_done = True
            for i in range(n):
                if len(words[i]) != 0:
                    is_done = False
                    break
        return True

# compare two words consecutively
# Runtime: 32 ms, faster than 78.00% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Verifying an Alien Dictionary.
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_idx = {c:idx for idx, c in enumerate(order)}
        n = len(words)
        for i in range(n-1):
            word1, word2 = words[i], words[i+1]
            n1, n2 = len(word1), len(word2)
            is_large = False
            for j in range(min(n1, n2)):
                if char_idx[word2[j]] < char_idx[word1[j]]:
                    return False
                elif char_idx[word2[j]] > char_idx[word1[j]]:
                    is_large = True
                    break
            if not is_large:
                if n1 > n2:
                    return False
        return True
            

    