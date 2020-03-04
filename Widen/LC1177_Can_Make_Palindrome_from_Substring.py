"""
1177. Can Make Palindrome from Substring
Given a string s, we make queries on substrings of s.

For each query queries[i] = [left, right, k], we may rearrange the substring s[left], ..., s[right], and then choose up to k of them to replace with any lowercase English letter. 

If the substring is possible to be a palindrome string after the operations above, the result of the query is true. Otherwise, the result is false.

Return an array answer[], where answer[i] is the result of the i-th query queries[i].

Note that: Each letter is counted individually for replacement so if for example s[left..right] = "aaa", and k = 2, we can only replace two of the letters.  (Also, note that the initial string s is never modified by any query.)

 

Example :

Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
Output: [true,false,false,true,true]
Explanation:
queries[0] : substring = "d", is palidrome.
queries[1] : substring = "bc", is not palidrome.
queries[2] : substring = "abcd", is not palidrome after replacing only 1 character.
queries[3] : substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
queries[4] : substring = "abcda", could be changed to "abcba" which is palidrome.
"""


# akuna capital
# a little bit tricky
# similar to the prefix_sum 
# Runtime: 3196 ms, faster than 11.18% of Python3 online submissions for Can Make Palindrome from Substring.
# Memory Usage: 65.5 MB, less than 100.00% of Python3 online submissions for Can Make Palindrome from Substring.
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(queries)
        res = [False for _ in range(n)]
        self.stat = self.cal_freq(s)
        # print(self.stat)
        for i, (left, right, val) in enumerate(queries):
            res[i] = self.check(left, right, val)
        return res
    
    def cal_freq(self, s):
        n = len(s)
        res = [[0 for _ in range(26)]]
        freq = collections.defaultdict(int)
        for i in range(1, n+1):
            freq[s[i-1]] += 1
            idx = ord(s[i-1]) - ord("a")
            tmp = res[-1].copy()
            tmp[idx] = tmp[idx] + 1
            res.append(tmp)
            
        return res 
    
    def check(self, left, right, k):
        half_len = (right-left+1) // 2
        if k >= half_len:
            return True
        freq = [self.stat[right+1][i] - self.stat[left][i] for i in range(26)]
        cnt = 0
        for i in range(26):
            if freq[i] % 2 == 1:
                cnt += 1
        return cnt // 2 <= k
    

# XOR solution
# basically use the principle
# even - even = even, odd - odd = even
# even - odd = odd, odd - even = odd
# just as XOR operation
# therefore we just need to use a 26-bit integer to represent if the occurance of that letter so far is even or odd
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        accu = [0] * ( len(s) + 1 )
        for i,c in enumerate(s):
            accu[i+1] = accu[i] ^ ( 1 << (ord(c) - ord("a")) )  
        return [ bin( accu[left] ^ accu[right+1] ).count("1") >> 1 <= k for left, right, k in queries ]
    