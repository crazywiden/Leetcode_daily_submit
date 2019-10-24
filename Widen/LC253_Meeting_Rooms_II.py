"""
LC253 Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""


# priority queue algorithm
# need to study more about it
# Runtime: 52 ms, faster than 98.38% of Python online submissions for Meeting Rooms II.
# Memory Usage: 15 MB, less than 100.00% of Python online submissions for Meeting Rooms II.
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[0])
        heap = []
        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                # room is already used in last meeting and continue to use the same room for this meeting
                heapq.heapreplace(heap, interval[1])
                
            else:
                heapq.heappush(heap, interval[1])
                
        return len(heap)
        