"""
321. Create Maximum Number
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.
"""

# simple math problem
# Runtime: 420 ms, faster than 69.02% of Python3 online submissions for Create Maximum Number.
# Memory Usage: 14 MB, less than 53.99% of Python3 online submissions for Create Maximum Number.
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def getK(nums, k):
            n = len(nums)
            to_pop = n - k
            ans = []
            for num in nums:
                while len(ans) > 0 and num > ans[-1] and to_pop > 0:
                    to_pop -= 1
                    ans.pop()
                ans.append(num)
            return ans[:k]

        def getMax(nums1, nums2):
            ans = []
            while nums1 and nums2:
                if nums1 > nums2:
                    ans.append(nums1.pop(0))
                else:
                    ans.append(nums2.pop(0))
            if nums1:
                ans += nums1
            else:
                ans += nums2
            return ans

        n1 = len(nums1)
        n2 = len(nums2)
        ans = []
        for k1 in range(k+1):
            k2 = k - k1
            if k1 > n1 or k2 > n2:
                continue
            ans = max(ans, getMax(getK(nums1, k1), getK(nums2, k2)))
        return ans