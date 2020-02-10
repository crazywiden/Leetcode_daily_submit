"""
986. Interval List Intersections
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
"""

# SWEEP line method
# Runtime: 172 ms, faster than 22.99% of Python3 online submissions for Interval List Intersections.
# Memory Usage: 14 MB, less than 6.06% of Python3 online submissions for Interval List Intersections.
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        indices = []
        for start, end in A:
            indices.append([start, 1])
            indices.append([end, -1])
        for start, end in B:
            indices.append([start, 1])
            indices.append([end, -1])
        indices = sorted(indices, key=lambda x:(x[0], -x[1]))
        
        start = -1
        res = []
        num_interval = 0
        for index, is_start in indices:
            if is_start == 1:
                start = max(index, start)
                num_interval += 1
            else:
                if start != -1 and num_interval > 1:
                    res.append([start, index])
                    start = -1
                num_interval -= 1
        return res      