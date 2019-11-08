"""
LC1060 -- Missing Element in Sorted Array
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
"""


# Runtime: 348 ms, faster than 61.22% of Python3 online submissions for Missing Element in Sorted Array.
# Memory Usage: 19.2 MB, less than 100.00% of Python3 online submissions for Missing Element in Sorted Array


# binary search
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0] + k
        self.nums = nums
        start, end = 0, len(nums) - 1  # start, end are all indices
        return self.binary_search(start, end, k)
    
    def binary_search(self, start, end, k):
        if end - start == 1:
            num_should_have = self.nums[end] - self.nums[start] + 1
            num_missing = num_should_have - 2
            if num_missing < k:
                return self.nums[end] + (k-num_missing)
            else:
                return self.nums[start] + k
        mid = (start + end) // 2
        # the following two lines can be simplified
        num_should_have_left = self.nums[mid] - self.nums[start] + 1
        num_missing = num_should_have_left - (mid - start + 1)
        if num_missing == k:
            return self.nums[mid] - 1
        elif num_missing < k:
            return self.binary_search(mid, end, k-num_missing)
        else:
            return self.binary_search(start, mid, k)

# Runtime: 304 ms, faster than 99.71% of Python3 online submissions for Missing Element in Sorted Array.
# Memory Usage: 19.2 MB, less than 100.00% of Python3 online submissions for Missing Element in Sorted Array.
# no recursion version
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r+1)//2
            if nums[mid]-nums[0]-mid < k:
                l=mid
            else:
                r=mid-1
        return nums[0]+k+l


# Runtime: 304 ms, faster than 99.71% of Python3 online submissions for Missing Element in Sorted Array.
# Memory Usage: 19.2 MB, less than 100.00% of Python3 online submissions for Missing Element in Sorted Array.
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx
                
        n = len(nums)
        # If kth missing number is larger than 
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1) 

        idx = 1
        # find idx such that 
        # missing(idx - 1) < k <= missing(idx)
        while missing(idx) < k:
            idx += 1

        # kth missing number is larger than nums[idx - 1]
        # and smaller than nums[idx]
        return nums[idx - 1] + k - missing(idx - 1)
            