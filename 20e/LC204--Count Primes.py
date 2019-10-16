'''
Time complexity: O(n), 1504 ms, 10%
Space complexity: O(n), 25.3 MB, 64%
'''
#method 1: traverse
class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        list_n = [1]*(n-1)
        for i in range(2,n):
            if list_n[i-1] == 1:
                res = res + 1
                k = i
                while k * i < n:
                    list_n[k * i-1]=0
                    k = k + 1
        return res


'''
Time complexity: O(sqrt(n)), 1116 ms, 24.70%
Space complexity: O(n), 25.4 MB, 64.27%
'''
#method 2: traverse to sqrt(n)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2: return 0
        res = 0
        list_n = [1]*(n-1)
        list_n[0] = 0
        for i in range(2,int(n**0.5)+1):
            if list_n[i-1] == 1:
                k = i
                while k * i < n:
                    list_n[k * i-1]=0
                    k = k + 1
        return sum(list_n)