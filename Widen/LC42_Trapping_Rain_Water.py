"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""



# three pass
# time complexity -- O(N)
# Runtime: 56 ms, faster than 82.34% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 13.4 MB, less than 97.67% of Python3 online submissions for Trapping Rain Water.
class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left_max = [0 for _ in range(N)]
        right_max = [0 for _ in range(N)]
        curr_max = float("-inf")
        for i in range(N):
            if height[i] > curr_max:
                curr_max = height[i]
            left_max[i] = curr_max
            
        curr_max = float("-inf")
        for i in range(N-1, -1, -1):
            if height[i] > curr_max:
                curr_max = height[i]
            right_max[i] = curr_max
        
        res = 0
        for i in range(N):
            res += min(left_max[i], right_max[i]) - height[i]
            
        return res
            
# add space complexity -- O(1) version
# Runtime: 36 ms, faster than 99.82% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 13.3 MB, less than 97.67% of Python3 online submissions for Trapping Rain Water.
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        left, right = 0, n-1
        left_max, right_max = height[left], height[right]
        res = 0
        while left <= right:
            if left_max < right_max:
                
                left_max = max(left_max, height[left])
                res += left_max - height[left]
                left += 1 
                # if left_max > height[left]:
                #     res += left_max - height[left]
                # else:
                #     left_max = height[left]
            else:
                right_max = max(right_max, height[right])
                res += right_max - height[right]
                right -= 1
                # if right_max > height[right]:
                #     res += right_max - height[right]
                # else:
                #     right_max = height[right]
            # print(res)
        return res