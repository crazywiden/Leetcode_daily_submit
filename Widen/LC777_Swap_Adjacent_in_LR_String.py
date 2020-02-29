"""
777. Swap Adjacent in LR String
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Note:

1 <= len(start) = len(end) <= 10000.
Both start and end will only consist of characters in {'L', 'R', 'X'}.
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
    