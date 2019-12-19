"""
759. Employee Free Time
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
"""

# Line Swap method
# if we met a start, cnt += 1
# if we met an end, cnt -= 1
# time complexity -- O(NlogN), need sort all intervals
# Runtime: 96 ms, faster than 87.95% of Python3 online submissions for Employee Free Time.
# Memory Usage: 14.7 MB, less than 25.00% of Python3 online submissions for Employee Free Time.
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        START, END = 0, 1
        all_interval = []
        for person in schedule:
            for interval in person:
                all_interval.append((interval.start, START))
                all_interval.append((interval.end, END))
        
        all_interval = sorted(all_interval, key=lambda x: x[0])
        prev = None
        cnt = 0
        res = []
        for i in range(len(all_interval)):
            if cnt == 0 and prev is not None:
                if prev != all_interval[i][0]:
                    res.append(Interval(prev, all_interval[i][0]))
            if all_interval[i][1] == START:
                cnt += 1
            else:
                cnt -= 1
            prev = all_interval[i][0]
        return res



# priority queue
# if the current end is less than the smallest start
# then means there is a free time 
# use priority queue to maintain the smallest start
# also only stort one of jobs of each person in the queue to save memory
# time complexity  -- O(NlogC), C is the number of employee
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        res = []
        job_start_q = [(emp[0].start, emp_id, 0) for emp_id, emp in enumerate(schedule)]
        heapq.heapify(job_start_q)
        largest_end = min(interval.start for emp in schedule for interval in emp)
        while job_start_q:
            start, emp_id, job_id = heapq.heappop(job_start_q)
            if largest_end < start:
                res.append(Interval(largest_end, start))
            largest_end = max(largest_end, schedule[emp_id][job_id].end)
            if job_id + 1 < len(schedule[emp_id]):
                heapq.heappush(job_start_q, (schedule[emp_id][job_id+1].start, emp_id, job_id+1))
        return res



