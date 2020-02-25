"""
1062. Longest Repeating Substring
Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

 

Example 1:

Input: "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
Example 4:

Input: "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.
"""
# a very intereting question
# basic idea is to do binary search of the answer
# but a question is : what is the time complexity of hash a string in Python
# answer is O(N)
# so use the following method, the time complexity is O((N-L)L log N)
# log N is the time complexity to binary search result
# N-L is the time complexity to traverse the whole string
# L is the time complexity to hash a string segment 
# we can speed up the hash time complexity using Rabin-Karp method -- idea of rolling hash
# Runtime: 2500 ms, faster than 8.93% of Python3 online submissions for Longest Repeating Substring.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Longest Repeating Substring.
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        left, right = 0, n-1
        while left <= right:
            mid = left + (right-left) // 2
            if self.validate(s, mid):
                left += 1 
            else:
                right -= 1 
        return right
    
    def validate(self, s, L):
        hash_dict = set([])
        for i in range(L, len(s)+1):
            if s[i-L:i] in hash_dict:
                return True
            hash_dict.add(s[i-L:i])
        return False


# rolling hash
# funny thing is in rolling hash, TLE...
# maybe the module is too time-comsumption
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        self.MOD = 10**9 + 7
        n = len(s)
        left, right = 0, n-1
        while left <= right:
            mid = left + (right-left) // 2
            if self.validate(s, mid):
                left += 1 
            else:
                right -= 1 
        return right
    
    def validate(self, s, L):
        hash_dict = set([])
        prev_hash = None
        prev_letter = None
        for i in range(L, len(s)+1):
            hash_val = self.cal_hash(s[i-L:i], prev_hash, prev_letter)
            if hash_val in hash_dict:
                return True
            hash_dict.add(hash_val)
            prev_hash = hash_val
            prev_letter = s[i-L]
        return False
    
    def cal_hash(self, s, prev_hash=None, prev_letter=None):
        level = len(s)-1
        if not prev_hash:
            val = 0
            for i in range(len(s)):
                val += (ord(s[i])-96) * 26 ** (level-i)
            # return val
            return val % self.MOD
        # return (prev_hash-(ord(prev_letter)-96)*((26**level)))*26 + (ord(s[-1])-96)
        hash_val = (prev_hash-(ord(prev_letter)-96)*((26**level) % self.MOD))*26 + (ord(s[-1])-96)
        return hash_val % self.MOD
                
        
        