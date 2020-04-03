"""
763. Partition Labels
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""

# bug free!!
# time complexity -- O(n)
# Runtime: 32 ms, faster than 88.36% of Python3 online submissions for Partition Labels.
# Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for Partition Labels.
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_idx = collections.defaultdict(int)
        for idx, char in enumerate(S):
            last_idx[char] = idx
        res = []
        prev_split = -1
        curr_max = -1
        for i, char in enumerate(S):
            curr_max = max(curr_max, last_idx[char])
            if i >= curr_max:
                curr_len = i - prev_split
                prev_split = i
                res.append(curr_len)
                if i < len(S) - 1:
                    curr_max = last_idx[S[i+1]]
        return res
    
                
                