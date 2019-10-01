#reference：https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode/
'''
Time complexity: O(lgn), 120 ms, 76.70%
Space complexity: O(n), 13.9 MB, 5.26% ？
'''
#method1: mathematical derivation
#reference: https://leetcode-cn.com/problems/reach-a-number/solution/pythonchao-ji-jian-ji-de-jie-fa-by-zhengkang/
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        i=0
        max_t=0
        while max_t < target or (max_t+target)%2 !=0 :
            i=i+1
            max_t=max_t+i
        return i