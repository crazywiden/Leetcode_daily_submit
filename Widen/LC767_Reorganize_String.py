"""
767. Reorganize String
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""

# time complexity -- O(n^2)
# Runtime: 32 ms, faster than 58.26% of Python3 online submissions for Reorganize String.
# Memory Usage: 13.9 MB, less than 14.29% of Python3 online submissions for Reorganize String.
class Solution:
    def reorganizeString(self, S: str) -> str:
        freq = [[char, f] for char, f in collections.Counter(S).items()]
        freq = sorted(freq, key=lambda x:x[1])
        res = ""
        left, right = 0, len(freq)-1
        while left < right:
            if freq[left][1] < freq[right][1]:
                base = freq[left][1]
                freq[left][1] = 0
                freq[right][1] -= base
                res += (freq[right][0] + freq[left][0]) * base
                left += 1
            elif freq[left][1] > freq[right][1]:
                base = freq[right][1]
                freq[right][1] = 0
                freq[left][1] -= base
                res += (freq[right][0] + freq[left][0]) * base
                right -= 1
            else:
                base = freq[right][1]
                freq[right][1] = 0
                freq[left][1] = 0
                res += (freq[right][0] + freq[left][0]) * base
                left += 1
                right -= 1
        if freq[left][1] > len(res):
            return ""
        if freq[left][1] == 0:
            return res
        
        if freq[left][0] != res[0]:
            res = freq[left][0] + res
            freq[left][1] -= 1
            anchor = 2
        else:
            anchor = 1

        
        while freq[left][1] > 0 and anchor < len(res):
            if res[anchor-1] == freq[left][0]:
                anchor += 1
                continue
            if res[anchor] == freq[left][0]:
                anchor += 2
                continue
                
            res = res[:anchor] + freq[left][0] + res[anchor:]
            anchor += 2
            freq[left][1] -= 1
        
        if freq[left][1] == 1:
            if res[-1] == freq[left][0]:
                return ""
            res += freq[left][0]
            freq[left][1] -= 1
        if freq[left][1] > 0:
            return ""
        return res
    
            
            

    
    
        