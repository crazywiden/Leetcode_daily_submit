"""
LC651 4 Keys Keyboard
Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.
"""

# 1d dp
# Runtime: 40 ms, faster than 58.78% of Python3 online submissions for 4 Keys Keyboard.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for 4 Keys Keyboard.
class Solution:
    def maxA(self, N: int) -> int:
        if N <= 10:
            k = (N-1)//2
            return max(N, (N-1)*k-k**2)
        
        dp = [0 for _ in range(N+1)]
        for i in range(11):
            k = (i-1)//2
            dp[i] = max(i, (i-1)*k-k**2)
            
        for i in range(11, N+1):
            for j in range(1, i-2):
                dp[i] = max(dp[i], dp[j]*(i-j-2)+dp[j])
        return dp[N]