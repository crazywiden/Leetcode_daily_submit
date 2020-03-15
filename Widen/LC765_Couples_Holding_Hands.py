"""
765. Couples Holding Hands
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
"""
# tutorial: https://leetcode.com/articles/couples-holding-hands/
# Runtime: 36 ms, faster than 20.78% of Python3 online submissions for Couples Holding Hands.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Couples Holding Hands.
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # this is actually a math problem
        # key part: to prove why greedy is optimal
        # greedy method:
        # find the couple, then put the couple on his / her right
        # little trick: use x ^ 1 to find couple
        res = 0
        IDX = {ele:idx for idx, ele in enumerate(row)}
        for i in range(0, len(row), 2):
            couple = row[i] ^ 1
            couple_idx = IDX[couple]
            if couple_idx - i == 1:
                continue
            row[i+1], row[couple_idx] = row[couple_idx], row[i+1]
            IDX = {ele:idx for idx, ele in enumerate(row)}
            res += 1
        return res
            