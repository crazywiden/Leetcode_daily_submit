"""
1231. Divide Chocolate

You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

 

Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
"""

# tutorial: https://www.cnblogs.com/fish1996/p/11742860.html
# better way is to use binary search, which is much more brilliant!
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        # binary search
        left, right = min(sweetness), sum(sweetness)
        while right - left > 1:
            mid = (left + right) // 2
            # print(left, right, mid)
            if self.check(sweetness, K, mid):
                left = mid
                # print("go right")
            else:
                right = mid - 1
                # print("go left")
        if self.check(sweetness, K, right):
            return right
        return left
    
    def check(self, arr, K, val):
        seg_sum = 0
        num_seg = 0
        for i in range(len(arr)):
            seg_sum += arr[i]
            if seg_sum >= val:
                seg_sum = 0
                num_seg += 1
        return num_seg >= K+1



# dp but TLE
# time complexity -- O(N^2)
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        # dp solution
        n = len(sweetness)
        dp = [[0 for _ in range(K+1)] for _ in range(n)]
        one_piece_sum = 0
        for i in range(n):
            one_piece_sum += sweetness[i]
            dp[i][0] = one_piece_sum
            
        for k in range(1, K+1):
            for i in range(k-1, n):
                last_sum = 0
                for j in range(i-1, k-2, -1):
                    last_sum += sweetness[j+1]
                    dp[i][k] = max(dp[i][k], min(dp[j][k-1], last_sum))
                    
        return dp[n-1][K]