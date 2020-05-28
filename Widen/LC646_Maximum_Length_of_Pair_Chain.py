"""
646. Maximum Length of Pair Chain
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
"""

# turns out this is a greedy problem, sorted by the second parameter!
# time complexity -- O(NlogN)
# a good example as comparsion between greedy and dp
# Runtime: 204 ms, faster than 97.11% of Python3 online submissions for Maximum Length of Pair Chain.
# Memory Usage: 14.1 MB, less than 7.14% of Python3 online submissions for Maximum Length of Pair Chain.
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        res = 0
        curr = float("-inf")
        for x, y in sorted(pairs, key=lambda x:x[1]):
            if curr >= x:
                continue
            curr = y
            res += 1
        return res
        


# time complexity -- O(N^2 + NlogN)
# Runtime: 3992 ms, faster than 7.44% of Python3 online submissions for Maximum Length of Pair Chain.
# Memory Usage: 14.2 MB, less than 7.14% of Python3 online submissions for Maximum Length of Pair Chain.
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        N = len(pairs)
        self.pairs = sorted(pairs, key = lambda x:x[0])
        self.visited = [False for _ in range(N)]
        self.lens = [1 for _ in range(N)]
        res = -1
        for i in range(N):
            res = max(res, self.dfs(i, N))
        return res
    
    def dfs(self, start_idx, N):
        if self.visited[start_idx]:
            return self.lens[start_idx]
        self.visited[start_idx] = True
        if start_idx == N - 1:
            return 1
        base_len = 0
        for i in range(start_idx, N):
            if self.pairs[i][0] <= self.pairs[start_idx][1]:
                continue
            tmp_max_len = self.dfs(i, N)
            base_len = max(base_len, tmp_max_len)
        self.lens[start_idx] = base_len + 1
        return self.lens[start_idx]
    
            
        