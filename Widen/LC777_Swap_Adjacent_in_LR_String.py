"""
777. Swap Adjacent in LR String
"""

# more like a brain teaser...
# Runtime: 40 ms, faster than 89.02% of Python3 online submissions for Swap Adjacent in LR String.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Swap Adjacent in LR String.
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        if start.replace("X", "") != end.replace("X",""):
            return False
        n = len(start)
        start_p, end_p = 0, 0
        while start_p < n or end_p < n:
            while start_p < n and start[start_p] == "X":
                start_p += 1 
            while end_p < n and end[end_p] == "X":
                end_p += 1 
            if start_p >= n or end_p >= n:
                break
            if start[start_p] != end[end_p]:
                return False
            if start[start_p] == "R" and start_p > end_p:
                return False
            if start[start_p] == "L" and start_p < end_p:
                return False
            start_p += 1
            end_p += 1
        return True 
    