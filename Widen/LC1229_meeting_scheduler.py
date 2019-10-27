"""
LC1229 meeting scheduler
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

 

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []
"""


# solved by myself!!
# schedule problem using priority queue would be very efficient
# Runtime: 592 ms, faster than 87.55% of Python3 online submissions for Meeting Scheduler.
# Memory Usage: 21.1 MB, less than 100.00% of Python3 online submissions for Meeting Scheduler.
import heapq
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.extend(slots2)
        slots1 = sorted(slots1, key=lambda x:x[0])
        queue = []
        heapq.heappush(queue, slots1[0][1])
        for interval in slots1[1:]:
            end = interval[0] + duration
            if queue and interval[0] < queue[0]:
                if (end <= queue[0]) and (end <= interval[1]):
                    return [interval[0], end]
            heapq.heappushpop(queue, interval[1])
        return []