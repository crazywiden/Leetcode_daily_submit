"""
56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
# Runtime: 92 ms, faster than 79.23% of Python3 online submissions for Merge Intervals.
# Memory Usage: 14.6 MB, less than 6.52% of Python3 online submissions for Merge Intervals.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x:x[0])
        left, right = 0, 1
        res = [intervals[0]]
        while right < len(intervals):
            left_node = res[-1]
            right_node = intervals[right]
            if left_node[1] >= right_node[0]: # can be merge
                res[-1][1] = max(left_node[1], right_node[1])
                right += 1
            else:
                res.append(right_node)
                right += 1
        return res
                