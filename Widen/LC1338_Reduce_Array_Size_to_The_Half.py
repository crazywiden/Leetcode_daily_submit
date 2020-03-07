"""
1338. Reduce Array Size to The Half
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

 

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
"""
# sorting method
# time complexity -- O(nlog n)
# also have a bucket sort method, whose time complexity is O(N)
# didn't implemented yet
# Runtime: 592 ms, faster than 96.37% of Python3 online submissions for Reduce Array Size to The Half.
# Memory Usage: 29.4 MB, less than 100.00% of Python3 online submissions for Reduce Array Size to The Half.
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = collections.Counter(arr)
        thres = (len(arr)+1) // 2
        cnt_len = 0
        for idx, val in enumerate(sorted(freq.values(), reverse=True)):
            cnt_len += val 
            if cnt_len >= thres:
                break
        return idx + 1