'''
Time complexity: O(n),108 ms, 99.03%
Space complexity: O(n), 20.5 MB, 17.14%
'''
#method 1: list
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        a = list(range(1,n+1))
        a = map(str,a)
        a = sorted(list(a))
        return a
