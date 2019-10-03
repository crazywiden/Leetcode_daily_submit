'''
Time complexity: O(2^n),888 ms,27.27%？
Space complexity: O(n),13.8 MB,5.54%
'''
#method1: recursion
class Solution:
    def fib(self, N: int) -> int:
        if N == 0: return 0
        if N == 1: return 1
        return self.fib(N-1)+self.fib(N-2)


'''
Time complexity: O(n),40 ms,94.57%
Space complexity: O(n),13.7 MB,5.54%
'''
#method2: iteration(matrix calculation)
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:return 0
        a1 = 0
        a2 = 1
        i = 1
        while i < N:
            [a1,a2]=[a2,a1+a2]
            i = i+1
        return a2

#reference:https://leetcode-cn.com/problems/fibonacci-number/solution/javascriptjie-fa-by-abpvnext/
'''
Time complexity: O(1),36 ms,98.77%
Space complexity: O(1),13.8 MB,5.54%
'''
#method3: mathematic formula
class Solution:
    def fib(self, N: int) -> int:
        a = 5**(1/2)
        return int((((1+a)/2)**N-((1-a)/2)**N)/a)


