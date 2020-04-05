"""
1163. Last Substring in Lexicographical Order
Given a string s, return the last substring of s in lexicographical order.

 

Example 1:

Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
Example 2:

Input: "leetcode"
Output: "tcode"
 

Note:

1 <= s.length <= 4 * 10^5
s contains only lowercase English letters.
"""
# big lao solution
# Runtime: 148 ms, faster than 99.37% of Python3 online submissions for Last Substring in Lexicographical Order.
# Memory Usage: 20.1 MB, less thanc 100.00% of Python3 online submissions for Last Substring in Lexicographical Order.
class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        max_indices = []
        max_char = max(set(s))
        consecutive = False
        for idx, char in enumerate(s):
            if char == max_char:
                if not consecutive:
                    max_indices.append(idx)
                    consecutive = True
            else:
                consecutive = False
                
        increment = 1
        while len(max_indices) > 1:
            new_indices = []
            base_char = ""
            for idx in max_indices:
                if idx + increment < n:
                    new_char = s[idx+increment]
                else:
                    new_char = ""
                if new_char > base_char:
                    new_indices = [idx]
                    base_char = new_char
                elif new_char == base_char:
                    new_indices.append(idx)
            max_indices = new_indices.copy()
            increment += 1
        return s[max_indices[0]:]
    
                
        

# brutal force
# Runtime: 2416 ms, faster than 25.05% of Python3 online submissions for Last Substring in Lexicographical Order.
# Memory Usage: 33.9 MB, less than 100.00% of Python3 online submissions for Last Substring in Lexicographical Order.
class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        sub_str = collections.defaultdict(list)
        for idx, char in enumerate(s):
            sub_str[char].append(idx)
        max_key = sorted(sub_str.keys())[-1]
        res = ""
        for idx in sub_str[max_key]:
            tmp_str = s[idx:]
            if tmp_str > res:
                res = tmp_str
        return res
    