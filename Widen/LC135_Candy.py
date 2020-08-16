"""
135. Candy
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""

# more like a math problem
# should be medium level
# time complexity -- O(N)
# Runtime: 180 ms, faster than 69.60% of Python3 online submissions for Candy.
# Memory Usage: 16.4 MB, less than 39.19% of Python3 online submissions for Candy.
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1]*len(ratings)
        lbase, rbase = 1, 1

        for i in range(1, len(ratings)):  
            lbase = lbase + 1 if ratings[i] > ratings[i-1] else 1
            res[i] = lbase

        for i in range(len(ratings)-2, -1, -1): 
            rbase = rbase + 1 if ratings[i] > ratings[i+1] else 1
            res[i] = max(rbase, res[i])
        return sum(res)