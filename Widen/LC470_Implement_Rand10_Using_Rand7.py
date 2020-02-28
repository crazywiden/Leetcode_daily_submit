"""
470. Implement Rand10() Using Rand7()
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().

 

Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]
"""


# quite interesting question
# use the knowlege about rejection sampling
# see tutorial: https://leetcode.com/articles/implement-rand10-using-rand7/
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        row, col = rand7(), rand7()
        index = 7 * (row-1) + col
        while index > 40:
            row, col = rand7(), rand7()
            index = 7 * (row-1) + col
        return (index-1) % 10 + 1
        