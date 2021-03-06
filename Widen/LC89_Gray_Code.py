"""
LC89. Gray Code
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
"""

# Runtime: 40 ms, faster than 22.57% of Python3 online submissions for Gray Code.
# Memory Usage: 14.7 MB, less than 5.26% of Python3 online submissions for Gray Code.
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = {}
        curr = "0" * n
        self.dfs(res, curr, n, 0)
        return [int(key, 2) for key,_ in sorted(res.items(), key=lambda x:x[1])]
        
    
    def dfs(self, res, curr, n, index):
        res[curr] = index
        for i in range(n):
            if curr[i] == "0":
                tmp = curr[:i] + "1" + curr[i+1:]
            else:
                tmp = curr[:i] + "0" + curr[i+1:]
            if tmp in res:
                continue
                
            self.dfs(res, tmp, n, index+1)
            break
            
    