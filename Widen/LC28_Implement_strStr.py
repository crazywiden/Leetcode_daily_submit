"""
28. Implement strStr()
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""
# Runtime: 1596 ms, faster than 6.75% of Python3 online submissions for Implement strStr().
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Implement strStr().

#  Rabin-Karp algorithm
# should be O(N)
# but don't know why so bad...
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        using Rabin-Karp algorithm
        """
        if not needle:
            return 0
        base = 2
        k = len(needle)
        if len(haystack) < k:
            return -1
        hash_val = 0
        base_hash_val = 0
        for i in range(k):
            hash_val += ord(haystack[i]) * (base**(k-i-1))
            base_hash_val += ord(needle[i]) * (base**(k-i-1))
        
        if hash_val == base_hash_val:
            return 0
        for i in range(k, len(haystack)):
            hash_val = (hash_val-ord(haystack[i-k])*(base**(k-1)))*base+ord(haystack[i])
            if hash_val == base_hash_val:
                return i - k + 1
        return -1


# a better way...
# turns out build-in function is better...
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        