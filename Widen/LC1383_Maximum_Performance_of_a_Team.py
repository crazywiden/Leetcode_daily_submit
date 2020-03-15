"""
1383. Maximum Performance of a Team
There are n engineers numbered from 1 to n and two arrays: speed and efficiency, where speed[i] and efficiency[i] represent the speed and efficiency for the i-th engineer respectively. Return the maximum performance of a team composed of at most k engineers, since the answer can be a huge number, return this modulo 10^9 + 7.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers. 

 

Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
Example 2:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
Example 3:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
"""

# first time do a leetcode contest
# should have solved this problem
# at first thought it was dp, but turns out just a simple heap problem
# should open your mind and don't panic
# Runtime: 432 ms, faster than 66.67% of Python3 online submissions for Maximum Performance of a Team.
# Memory Usage: 34 MB, less than 100.00% of Python3 online submissions for Maximum Performance of a Team.
import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        pair = [(ele1, ele2) for ele1, ele2 in zip(efficiency, speed)]
        pair = sorted(pair, key=lambda x:-x[0])
        heap = [pair[0][1]]
        heapq.heapify(heap)
        all_speed = sum(heap)
        res = pair[0][0] * pair[0][1]
        for i in range(1, n):
            if len(heap) >= k:
                if pair[i][1] < heap[0]:
                    continue
                ele = heapq.heappop(heap)
                heapq.heappush(heap, pair[i][1])
            else:
                heapq.heappush(heap, pair[i][1])
                ele = 0
            all_speed = all_speed - ele + pair[i][1]
            res = max(res, all_speed*pair[i][0])
        return res % MOD
    
            
        