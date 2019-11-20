"""
658. Find K Closest Elements
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
"""


# binary search + two pointers
# Runtime: 348 ms, faster than 74.84% of Python3 online submissions for Find K Closest Elements.
# Memory Usage: 14.1 MB, less than 91.67% of Python3 online submissions for Find K Closest Elements.
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search + two pointers
        if arr[0] >= x:
            return arr[:k]
        
        # find the largest element that is less than x
        left, right = 0, len(arr)
        while left < right-1:
            mid = (left + right) // 2
            if arr[mid] == x:
                left = mid
                break
            if arr[mid] < x:
                left = mid
            else:
                right = mid - 1
        right = left + 1
        res = []
        for i in range(k):
            if self.is_left_closer(left, right, arr, x):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
        return sorted(res)
    
    def is_left_closer(self, left, right, arr, x):
        if left < 0:
            return False
        if right >= len(arr):
            return True
        return x - arr[left] <= arr[right] - x
        