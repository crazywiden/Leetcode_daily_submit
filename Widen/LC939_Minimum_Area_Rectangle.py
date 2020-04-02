"""
939. Minimum Area Rectangle
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""

# first find two points that can determine a rectangle -- left bottom point and right top point
# time complexity -- O(n^2)
# the following code has much potential to be improved
# Runtime: 2428 ms, faster than 18.09% of Python3 online submissions for Minimum Area Rectangle.
# Memory Usage: 14.2 MB, less than 19.05% of Python3 online submissions for Minimum Area Rectangle.
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        area = float("inf")
        hash_points = set([])
        n = len(points)
        for x, y in points:
            hash_points.add((x, y))
        
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 >= x2 or y1 >= y2:
                    continue
                if (x1, y2) in hash_points and (x2, y1) in hash_points:
                    area = min(area, (x2-x1)*(y2-y1))
        if area == float("inf"):
            return 0
        return area
