"""
1055. Shortest Way to Form String
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
Accepted
"""
Runtime: 24 ms, faster than 99.87% of Python3 online submissions for Shortest Way to Form String.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Shortest Way to Form String.
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        N = len(target)
        dp = [1 for _ in range(N+1)]
        dp[0] = 0
        cnt = 1
        for i in range(N):
            idx = source.find(target[i], dp[i])
            if idx != -1: # found the letter
                dp[i+1] = idx + 1
            else:
                new = source.find(target[i])
                if new != -1:
                    cnt += 1
                    dp[i+1] = new + 1
                else:
                    return -1
        return cnt