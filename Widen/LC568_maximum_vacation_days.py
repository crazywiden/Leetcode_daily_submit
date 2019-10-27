"""
LC568. Maximum Vacation Days
LeetCode wants to give one of its best employees the option to travel among N cities to collect algorithm problems. But all work and no play makes Jack a dull boy, you could take vacations in some particular cities and weeks. Your job is to schedule the traveling to maximize the number of vacation days you could take, but there are certain rules and restrictions you need to follow.

Rules and restrictions:
You can only travel among N cities, represented by indexes from 0 to N-1. Initially, you are in the city indexed 0 on Monday.
The cities are connected by flights. The flights are represented as a N*N matrix (not necessary symmetrical), called flights representing the airline status from the city i to the city j. If there is no flight from the city i to the city j, flights[i][j] = 0; Otherwise, flights[i][j] = 1. Also, flights[i][i] = 0 for all i.
You totally have K weeks (each week has 7 days) to travel. You can only take flights at most once per day and can only take flights on each week's Monday morning. Since flight time is so short, we don't consider the impact of flight time.
For each city, you can only have restricted vacation days in different weeks, given an N*K matrix called days representing this relationship. For the value of days[i][j], it represents the maximum days you could take vacation in the city i in the week j.
You're given the flights matrix and days matrix, and you need to output the maximum vacation days you could take during K weeks.
"""




# 2d dp
# first time finish a hard without any reference! and myself optimization!
# Runtime: 2432 ms, faster than 56.55% of Python3 online submissions for Maximum Vacation Days.
# Memory Usage: 14.2 MB, less than 50.00% of Python3 online submissions for Maximum Vacation Days.
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        if len(flights) == 0 or len(days) == 0:
            return 0
        
        n_city = len(flights)
        n_weeks = len(days[0])
        if n_weeks == 0:
            return 0
        
        # every one can stay at the same place
        for i in range(n_city):
            flights[i][i] = 1
            
        connect_origin = flights[0].copy()
        prev_days = [days[i][0] * flights[0][i] for i in range(n_city)]

        for i in range(1, n_weeks):
            new_days = [0 for _ in range(n_city)]
            for j in range(n_city):
                # update connect_origin
                for n in range(n_city):
                    if connect_origin[n] * flights[n][j] == 1:
                        connect_origin[j] = 1
                        break
                if connect_origin[j] != 0:
                    max_extra_days = max(prev_days[n]*flights[n][j] for n in range(n_city))
                    new_days[j] = days[j][i] + max(prev_days[j], max_extra_days)

            prev_days = new_days.copy()
            
        return max(prev_days)
                
                