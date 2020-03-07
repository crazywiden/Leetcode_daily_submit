"""
1326. Minimum Number of Taps to Open to Water a Garden
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.
"""
# similar to Jump Game II and Video Stitching
# tutorial: https://coordinate.wang/index.php/archives/2875/
# Runtime: 160 ms, faster than 57.18% of Python3 online submissions for Minimum Number of Taps to Open to Water a Garden.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Minimum Number of Taps to Open to Water a Garden.
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        idx_dist = collections.defaultdict(int)
        for idx, radius in enumerate(ranges):
            if radius == 0:
                continue
            left = max(idx-radius, 0)
            right = min(idx+radius, n)
            idx_dist[left] = max(idx_dist[left], right)
        prev, curr = -1, 0
        step = 0
        for i in range(n+1):
            if curr >= n:
                return step
            elif prev < i and i <= curr:
                prev, step = curr, step + 1
            elif i > curr:
                return -1
            curr = max(curr, idx_dist[i])
        