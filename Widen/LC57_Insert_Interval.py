"""
57. Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

# sweep line and greedy
# could have achieve O(N) by modify the sort part to a binary insertion
# Runtime: 84 ms, faster than 49.89% of Python3 online submissions for Insert Interval.
# Memory Usage: 17.5 MB, less than 8.00% of Python3 online submissions for Insert Interval.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        time_stamp = []
        for start, end in intervals:
            time_stamp.append([start, 1])
            time_stamp.append([end, -1])
        
        new_start = [newInterval[0], 1]
        new_end = [newInterval[1], -1]
        
        time_stamp.append(new_start)
        time_stamp.append(new_end)
        
        time_stamp = sorted(time_stamp, key=lambda x:(x[0], -x[1]))
        
        cnt = 0
        res = []
        tmp = []
        for t, is_start in time_stamp:
            if is_start == 1:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                tmp.append(t)
                res.append(tmp.copy())
                tmp = []
            elif cnt == 1:
                if is_start != 1:
                    continue
                tmp.append(t)
            elif cnt == 2:
                continue
        return res
                
        