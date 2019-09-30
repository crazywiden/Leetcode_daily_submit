#reference：https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode/
'''
Time complexity: O(2^n)
Space complexity: O(n)
'''
#method1: method of exhaustion
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb_stairs(0,n)
    def climb_stairs(self,i:int, n:int) -> int:
        if i>n:
            return 0
        if i==n:
            return 1
        return self.climb_stairs(i+1,n)+self.climb_stairs(i+2,n)

#method2:https://leetcode-cn.com/problems/climbing-stairs/solution/solution-python3-by-bu-zhi-dao-gan-sha/
'''
need more time to look into
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [1,2]
        for i in range(2,n):
            f.append(f[i-1]+f[i-2])
        return f[n-1]
