'''
Time complexity: O(n),76 ms, 92.48%
Space complexity: O(n), 14 MB, 5.01%
'''
#method 1: compare half
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_l = list(str(x))
        x_len = len(x_l)
        if x_l[0]=="-": return False
        mid = int((x_len-1)/2)
        for i in range(mid+1):
            if x_l[i]!=x_l[x_len-1-i]:return False
        return True
