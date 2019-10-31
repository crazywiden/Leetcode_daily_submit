"""

LC358. Rearrange String k Distance Apart
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
"""


# this problem is not that hard... 
# my current bottleneck is: can't do a very efficient implementation
# next time should pay more attention on that
# solved by priority queue
# clearly not very efficient...
# Runtime: 148 ms, faster than 35.69% of Python3 online submissions for Rearrange String k Distance Apart.
# Memory Usage: 14.4 MB, less than 50.00% of Python3 online submissions for Rearrange String k Distance Apart.
import heapq
# class Solution:
#     def rearrangeString(self, s: str, k: int) -> str:
#         if len(s) == 0:
#             return ""
#         if len(s) == 1:
#             return s
#         if k == 0:
#             return s
        
#         freq = {}
#         for i in range(len(s)):
#             if s[i] not in freq:
#                 freq[s[i]] = 1
#             else:
#                 freq[s[i]] += 1
#         if len(freq) < k:
#             return ""
        
#         freq_queue = [[-value, key] for key, value in freq.items()]
#         heapq.heapify(freq_queue)
#         ans = ""
#         is_final = False
#         while freq_queue:
#             if len(freq_queue) < k:
#                 if is_final:
#                     return ""
#                 else:
#                     is_final = True
#             new_ele = []
#             for i in range(min(k, len(freq_queue))):
#                 ele = heapq.heappop(freq_queue)
#                 new_ele.append(ele)
#             for i in range(len(new_ele)):
#                 new_ele[i][0] += 1
#                 ans += new_ele[i][1]
#                 if new_ele[i][0] != 0:
#                     heapq.heappush(freq_queue, new_ele[i])
                    
#         return ans



import collections
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        n = len(s)
        if not k:
            return s
        count = collections.Counter(s)
        maxf = max(count.values())

        # count how many letters have the max_count
        count_maxf = sum(c == maxf for c in count.values())

        # if the string length is not enough to hold all the letters that have
        # the max_count, return ""
        if (maxf - 1) * (k-1) + count_maxf + maxf - 1 > len(s):
            return ""

        res = [None]*n
        i = (n - 1) % k
        for c in sorted(count, key=lambda i: -count[i]):
            for _ in range(count[c]):
                res[i] = c
                i += k
                if i >= n:
                    i = (i - 1) % k
        return "".join(res)



            