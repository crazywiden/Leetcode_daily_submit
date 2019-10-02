"""
LC413 -- Arithmetic Slices
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""

# relatively easy
# Runtime: 44 ms, faster than 77.36% of Python3 online submissions for Arithmetic Slices.
# Memory Usage: 14.1 MB, less than 6.67% of Python3 online submissions for Arithmetic Slices.
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        diff = A[1] - A[0]
        cnt = 2
        ans = 0
        for i in range(1, len(A) - 1):
            if A[i+1] - A[i] != diff:
                ans += (cnt-1)*(cnt-2)//2
                cnt = 2
                diff = A[i+1] - A[i]
            else:
                cnt += 1
        if diff == A[-1] - A[-2]:
            ans += (cnt-1)*(cnt-2)//2
            
        return ans