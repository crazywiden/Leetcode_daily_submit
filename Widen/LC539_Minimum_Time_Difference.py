"""
539. Minimum Time Difference
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""

# first sort then calculate smallest difference
# time complexity -- O(n log n)
# Runtime: 76 ms, faster than 58.48% of Python3 online submissions for Minimum Time Difference.
# Memory Usage: 16.7 MB, less than 100.00% of Python3 online submissions for Minimum Time Difference.
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_in_min = []
        for t in timePoints:
            t_in_min = self.transform(t)
            time_in_min.append(t_in_min)
        time_in_min = sorted(time_in_min)
        res = float("inf")
        for i in range(1, len(time_in_min)):
            diff = time_in_min[i] - time_in_min[i-1]
            res = min(diff, res)
        res = min(res, 24*60-time_in_min[-1] + time_in_min[0])
        return res
    
    def transform(self, t):
        h, m = t.split(":")
        return int(h) * 60 + int(m)
        