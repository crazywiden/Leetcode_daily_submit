"""
LC 457 -- Circular Array Loop
You are given a circular array nums of positive and negative integers. If a number k at an index is positive, 
then move forward k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, 
you may assume that the last element's next element is the first element, 
and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. 
A cycle must start and end at the same index and the cycle's length > 1. 
Furthermore, movements in a cycle must all follow a single direction. 
In other words, a cycle must not consist of both forward and backward movements.

 

Example 1:

Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
Example 2:

Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, 
because the cycle's length is 1. By definition the cycle's length must be greater than 1.
Example 3:

Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, 
because movement from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 is a backward movement. 
All movements in a cycle must follow a single direction.
"""

# naive method --  traverse all element one by one
# time complexity -- O(N^2)
# space complexity -- O(N)
# Runtime: 596 ms, faster than 24.03% of Python3 online submissions for Circular Array Loop.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Circular Array Loop.
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        def helper(init):
            visited_idx = {init}
            curr_idx = init
            if curr_idx + nums[curr_idx] >= 0:
                next_idx = (curr_idx + nums[curr_idx]) % N
            else:
                next_idx = N - abs(curr_idx + nums[curr_idx]) % N
                
            while next_idx not in visited_idx:
                visited_idx.add(next_idx)
                if nums[next_idx] * nums[init] < 0:
                    return False
                curr_idx = next_idx
                if curr_idx + nums[curr_idx] >= 0:
                    next_idx = (curr_idx + nums[curr_idx]) % N
                else:
                    next_idx = N - abs(curr_idx + nums[curr_idx]) % N
            if len(visited_idx) == 1:
                return False
            if curr_idx == next_idx:
                return False
            return True

        if N == 1:
            return False
        for i in range(N):
            
            if helper(i):
                return True
        return False
        
# method2 -- two pointers
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        visited = [False] * N
        
        for i in range(N):
            if not visited[i] and nums[i] != 0:
                path = set()
                direction = nums[i] // abs(nums[i])
                j = i
                while True:
                    next_j = (j + nums[j]) % N
                    if next_j in path:
                        return True
                    else:
                        path.add(j)
                        if next_j == j or direction * nums[next_j] <= 0 or visited[next_j]:
                            break
                        j = next_j
                for j in path:
                    visited[j] = True
        return False



            
