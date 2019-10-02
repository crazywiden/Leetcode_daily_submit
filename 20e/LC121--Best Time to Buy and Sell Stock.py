#reference：https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode/
'''
Time complexity: O(n)
Space complexity: O(1)
'''
#method1: for loop
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2: return 0
        res = 0
        for i in range(0,len(prices)-1):
            sell = max(prices[(i+1):])
            max_tmp = sell-prices[i]
            res = max(max_tmp,res)
        return res

'''
Time complexity: O(nlogn)?,1748 ms,6.37%
Space complexity: O(nlogn)?, 416.7 MB,5.32%
'''
#method2: recursion
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2: return 0
        p = prices.index(min(prices))
        left_pro = 0
        right_pro = 0
        left_l = prices[:p]
        right_l = prices[p:]
        if right_l: right_pro = max(right_l) - prices[p]
        if left_l:left_pro = self.maxProfit(left_l)
        if not left_l or (left_pro<=right_pro): return right_pro
        else: return left_pro


#method4: Dp
'''
Time complexity: O(n),80 ms,83.53%
Space complexity: O(1), 16.6 MB,5.32%
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<2: return 0
        d_pro = []
        for i in range(n-1):
            d_pro.append(prices[i+1]-prices[i])
        df =[[0] * 1 for i in range(n-1)]
        for i in range(n-1):
            if i==0:
                df[i]=max(0,d_pro[i])
                continue
            df[i] = max(0,df[i-1]+d_pro[i])
        return max(df)

#this is not the right solution for this problem, but a base for dp, just save this for future need
'''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        df =[[0] * 2 for i in range(n)]
        for i in range(n):
            if i==0:
                df[i][0]=0#base case
                df[i][1]=0-prices[i]#base case
                continue
            df[i][0] = max(df[i-1][0],df[i-1][1]+prices[i])#change case
            df[i][1] = max(df[i-1][1],df[i-1][0]-prices[i])#change case
        return df[n-1][0]
'''