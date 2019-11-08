"""
LC774. Minimize Max Distance to Gas Station
On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.

Example:

Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
"""

# TLE solution. sort of brutal force
import heapq
class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        diff = [-(stations[i]-stations[i-1]) for i in range(1, len(stations))]
        def dfs(dist_heap, k):
            # dist is a heapified list
            if k == 0:
                return dist_heap
            max_dist = heapq.heappop(dist_heap)
            cnt = 1
            curr_min = -max_dist
            while cnt <= k:
                new_dist_heap = dist_heap.copy()
                new_dist = max_dist / (cnt+1)
                for i in range(cnt+1):
                    heapq.heappush(new_dist_heap, new_dist)
                tmp_divide = dfs(new_dist_heap, k-cnt)
                if -tmp_divide[0] <= curr_min:
                    curr_dist = tmp_divide.copy()
                    curr_min = -tmp_divide[0]
                cnt += 1
            return curr_dist

        heapq.heapify(diff)
        diff = dfs(diff, K)
        return -diff[0]
        

# binary search of length
# so brilliant!!!
# reference: https://massivealgorithms.blogspot.com/2018/12/leetcode-774-minimize-max-distance-to.html
# Runtime: 680 ms, faster than 66.03% of Python3 online submissions for Minimize Max Distance to Gas Station.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Minimize Max Distance to Gas Station.
class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        left, right = 0, 10**8
        eps = 10**(-6)
        while right - left > eps:
            mid = (right + left)/2
            extra_cnt = self.cal_extra(stations, mid)
            if extra_cnt > K:
                left = mid
            else:
                right = mid
        return left
    
    def cal_extra(self, station, val):
        cnt = 0
        for i in range(1, len(station)):
            cnt += (station[i] - station[i-1])//val
        return cnt
                
# also very clever
# Runtime: 148 ms, faster than 99.52% of Python3 online submissions for Minimize Max Distance to Gas Station.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Minimize Max Distance to Gas Station.
import heapq, math
class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        n = len(stations)
        maxD = (stations[-1] - stations[0]) / (K+1)
        heap = []
        # push to heap such that distance is no more than maxD
        for i in range(n-1):
            dist = stations[i+1]-stations[i]
            stops = math.ceil(dist/maxD) - 1
            heapq.heappush(heap, (-dist/(stops+1), stops))
            K -= stops
            # print(heap)
            # print(K)
        
        # use the remaining stops
        for _ in range(K):
            dist, stops = heapq.heappop(heap)
            heapq.heappush(heap, (dist*(stops+1)/(stops+2), stops+1))
            # print(heap)
        return -heap[0][0]
                

