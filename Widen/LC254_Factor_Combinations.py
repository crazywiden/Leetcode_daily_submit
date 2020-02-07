"""
LC254 Factor Combinations
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""


# backtracking 
# reference -- https://www.cnblogs.com/grandyang/p/5332722.html
# actually pretty inefficient
# Runtime: 2600 ms, faster than 5.20% of Python3 online submissions for Factor Combinations.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Factor Combinations.
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        def helper(start, size, out):
            if size == 1:
                if len(out) > 1:
                    res.append(out.copy())
            else:
                for i in range(start, size+1):
                    if size % i == 0:
                        out.append(i)
                        helper(i, size//i, out)
                        out.pop()
        helper(2, n, [])
        return res





# a little optimization
# Runtime: 32 ms, faster than 97.33% of Python3 online submissions for Factor Combinations.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Factor Combinations.
import math
import copy
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        def helper(start, size, out):
            for i in range(start, 1+int(math.sqrt(size))):
                if size % i == 0:
                    new_out = copy.deepcopy(out)
                    new_out.append(i)
                    helper(i, size//i, new_out)
                    new_out.append(size//i)
                    res.append(new_out)
        helper(2, n, [])
        return res




# Runtime: 1432 ms, faster than 22.41% of Python3 online submissions for Factor Combinations.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Factor Combinations.
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n <= 2:
            return []
        
        res = []
        factors = []
        for i in range(2, n):
            if n % i == 0:
                factors.append(i)
                
        self.dfs(res, [], factors, n)
        return res
    
    def dfs(self, res, tmp, A, n):
        if n < 1:
            return 
        if n == 1:
            res.append(tmp.copy())
            return 
        
        for i in range(len(A)):
            tmp.append(A[i])
            self.dfs(res, tmp, A[i:], n / A[i])
            tmp.pop()
        




