"""
1094. Car Pooling
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
"""

# defferential array 
# so fast: https://www.cnblogs.com/COLIN-LIGHTNING/p/8436624.html
# Runtime: 52 ms, faster than 99.53% of Python3 online submissions for Car Pooling.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Car Pooling.
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        df_arr_len = -1
        for trip in trips:
            df_arr_len = max(df_arr_len, trip[2])
        df_arr = [0 for i in range(df_arr_len+1)]
        df_arr[0] = capacity
        
        for trip in trips:
            df_arr[trip[1]] -= trip[0]
            df_arr[trip[2]] += trip[0]
        acc = 0
        for i in range(len(df_arr)):
            acc += df_arr[i]
            if acc < 0:
                return False
        return True