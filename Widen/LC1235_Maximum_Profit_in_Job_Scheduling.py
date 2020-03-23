"""
1235. Maximum Profit in Job Scheduling
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime , endTime and profit arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:


Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
"""

# use heap to find the largest end time that smaller than current start time!
# so brilliant!
# time complexity -- O(n logn)
# Runtime: 556 ms, faster than 93.50% of Python3 online submissions for Maximum Profit in Job Scheduling.
# Memory Usage: 23.5 MB, less than 100.00% of Python3 online submissions for Maximum Profit in Job Scheduling.
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        all_ele = zip(startTime, endTime, profit)
        all_ele = sorted(all_ele, key=lambda x:x[0])
        
        heap = []
        curr_max = 0
        for start, end, val in all_ele:
            while heap and heap[0][0] <= start:
                _, prev_val = heapq.heappop(heap)
                curr_max = max(curr_max, prev_val)
            heapq.heappush(heap, (end, val+curr_max))
        return max([x[1] for x in heap])


# simple dp
# time complexity -- O(max(endTime)+ N log N)
# Runtime: 4952 ms, faster than 5.26% of Python3 online submissions for Maximum Profit in Job Scheduling.
# Memory Usage: 87.2 MB, less than 100.00% of Python3 online submissions for Maximum Profit in Job Scheduling.
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        all_ele = zip(startTime, endTime, profit)
        all_ele = sorted(all_ele, key=lambda x:x[1])
        max_time = all_ele[-1][1]
        dp = [0 for _ in range(max_time+1)]
        res = -1
        job_idx = 0
        for t in range(1, max_time+1):
            while job_idx < len(all_ele) and t == all_ele[job_idx][1]:
                start, end, val = all_ele[job_idx]
                job_idx += 1
                dp[t] = max(dp[t-1], dp[start] + val, dp[t])
                
            if job_idx == len(all_ele):
                res = max(res, dp[t])
                break
            if dp[t] == 0:
                dp[t] = dp[t-1]
            res = max(res, dp[t])
        return res
    
    
    