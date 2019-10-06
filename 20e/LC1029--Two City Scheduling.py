'''
Time complexity: O(logn)?,48 ms, 93.03%
Space complexity: O(n)?,13.7 MB, 100.00%
'''
#method1: mathematics
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        len_c = len(costs)
        sum_c = 0
        diff = []
        for i in range(len_c):
            sum_c = sum_c + costs[i][0]
            diff.append(costs[i][0]-costs[i][1])
        diff.sort(reverse=True)
        sum_c = sum_c - sum(diff[:int(len_c/2)])
        return sum_c