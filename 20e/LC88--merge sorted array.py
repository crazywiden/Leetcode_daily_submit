'''
Time complexity: O((n+m)log(n+m)),36 ms,99.57%
Space complexity: O(1),13.9 MB,5.07%
'''
#method1: take advantage of sorted lists
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2
        nums1 = nums1.sort()

'''
Time complexity: O((n+m)),52 ms,82.10%
Space complexity: O(1),13.9 MB,5.07%
'''
#method2: for loop
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m+n-1
        p_1 = m-1
        p_2 = n-1
        if m == 0:
            nums1[:n]=nums2[:n]
            n=-1
        if n > 0:
            while p>0:
                nums1[p]=max(nums1[p_1],nums2[p_2])
                p = p - 1
                if nums1[p_1] >= nums2[p_2]:
                    p_1 = p_1 - 1
                else: p_2 = p_2 - 1
                if p_1 < 0:
                    nums1[:p+1] = nums2[:p_2+1]
                    break
                if p_2 < 0: break