"""
659. Split Array into Consecutive Subsequences
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

 

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:

Input: [1,2,3,4,4,5]
Output: False
"""

# greedy again
# need to begin the summary 
# tutorial: https://medium.com/@dreamume/leetcode-659-split-array-into-consecutive-subsequences-a2828703cd4b
# Runtime: 596 ms, faster than 68.06% of Python3 online submissions for Split Array into Consecutive Subsequences.
# Memory Usage: 15 MB, less than 50.00% of Python3 online submissions for Split Array into Consecutive Subsequences.
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        freq = collections.defaultdict(int)
        tail = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1
            
        for num in nums:
            if freq[num] == 0:
                continue
            freq[num] -= 1
            if tail[num-1] > 0:
                tail[num-1] -= 1
                tail[num] += 1
            elif freq[num+1] > 0 and freq[num+2] > 0:
                freq[num+1] -= 1
                freq[num+2] -= 1
                tail[num+2] += 1
            else:
                return False
        return True
    
                