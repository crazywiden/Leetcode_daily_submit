"""
354. Russian Doll Envelopes
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""

# transform the problem into LIS 
# so brilliant!
# time complexity O(n log n)
# note: didn't use a package bisect so the rank doesen't look good 
# Runtime: 196 ms, faster than 19.93% of Python3 online submissions for Russian Doll Envelopes.
# Memory Usage: 15.3 MB, less than 20.00% of Python3 online submissions for Russian Doll Envelopes.
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # actually this is a LIS problem!
        envelopes = sorted(envelopes, key=lambda x:(x[0], -x[1]))
        all_ele = [x[1] for x in envelopes]
        return self.find_LIS(all_ele)
    
    def find_LIS(self, arr):
        n = len(arr)
        dp = [float("inf") for _ in range(n)]
        res = 0
        for ele in arr:
            insert_idx = self.binary_search(dp, ele)
            if insert_idx == res:
                res += 1
            dp[insert_idx] = ele
        return res
    
    def binary_search(self, arr, ele):
        left, right = 0, len(arr)-1 
        while left < right:
            mid = (left + right) // 2
            if arr[mid] >= ele:
                right = mid 
            else:
                left = mid + 1
        return right
    