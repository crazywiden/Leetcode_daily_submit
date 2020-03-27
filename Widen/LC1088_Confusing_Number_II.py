"""
1088. Confusing Number II
We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.

 

Example 1:

Input: 20
Output: 6
Explanation: 
The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
Example 2:

Input: 100
Output: 19
Explanation: 
The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
"""

# back tracking
# it's hard to think of back-tracking
# Runtime: 2904 ms, faster than 43.07% of Python3 online submissions for Confusing Number II.
# Memory Usage: 95.6 MB, less than 33.33% of Python3 online submissions for Confusing Number II.
class Solution:
    def confusingNumberII(self, N: int) -> int:
        useful = [0, 1, 6, 8, 9]
        res = 0
        self.change = {"0":"0", "1":"1", "6":"9", "9":"6", "8":"8"}
        res = self.dfs(N, useful, [1, 6, 8, 9])
        return res
    
    def dfs(self, N, useful, curr_list):
        if len(curr_list) == 0:
            return 0
        new_list = []
        res = 0
        for num in curr_list:
            if self.is_confusing(num):
                res += 1
            for ele in useful:
                new_num = num * 10 + ele
                if new_num > N:
                    continue
                new_list.append(new_num)
        res += self.dfs(N, useful, new_list)
        return res
            
    def is_confusing(self, num):
        str_num = str(num)
        left, right = 0, len(str_num) - 1
        while left <= right:
            if str_num[left] != self.change[str_num[right]]:
                return True
            left += 1
            right -= 1
        return False
