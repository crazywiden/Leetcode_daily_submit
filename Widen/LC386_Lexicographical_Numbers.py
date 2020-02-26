"""
386. Lexicographical Numbers
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""

# use idea of 10-branch tree
# Runtime: 116 ms, faster than 51.95% of Python3 online submissions for Lexicographical Numbers.
# Memory Usage: 18.5 MB, less than 100.00% of Python3 online submissions for Lexicographical Numbers.
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [0 for _ in range(n)]
        curr = 1
        for i in range(n):
            res[i] = int(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                if curr >= n:
                    curr = curr // 10
                curr += 1
                
                while curr % 10 == 0:
                    curr /= 10
        return res
    