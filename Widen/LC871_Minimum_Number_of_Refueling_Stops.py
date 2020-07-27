"""
871. Minimum Number of Refueling Stops
A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.
"""
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        
        if startFuel < stations[0][0]:
            return -1
        
        N  = len(stations)
        dp = [[0 for _ in range(target+1)] for _ in range(N)]
        # initialize
        last_dist = target - stations[-1][0]
        for i in range(target+1):
            if i >= last_dist:
                continue
            if i + stations[-1][1] < last_dist:
                dp[-1][i] = -1
                continue
            dp[-1][i] = 1
        # update
        for i in range(N-2, -1, -1):
            curr_dist = stations[i+1][0] - stations[i][0]
            for j in range(target+1):
                if j >= curr_dist:
                    dp[i][j] = dp[i+1][j-curr_dist]
                elif j + stations[i][1] < curr_dist:
                    return -1
                else:
                    left_gas = max(target, j+stations[i][1]-curr_dist)
                    if dp[i+1][left_gas] == -1:
                        return -1
                    dp[i][j] = 1 + dp[i+1][left_gas]
        return dp[0][stations[0][0]-startFuel]
