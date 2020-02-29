"""
670. Maximum Swap
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""

# my heart is so tired...
# time complexity -- O(nlogn)
# need to sort 
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        ele_pair = [[int(ele), idx] for idx, ele in enumerate(num)]
        ele_pair = sorted(ele_pair, key=lambda x: -x[0])
        hash_idx = collections.defaultdict(int)
        for i in range(len(ele_pair)):
            ele, idx = ele_pair[i]
            hash_idx[ele] = max(hash_idx[ele], idx)
        for i in range(len(ele_pair)):
            ele, idx = ele_pair[i]
            ele_pair[i][1] = hash_idx[ele]
        # print(hash_idx)
        # print(ele_pair)
        for i, (ele, idx) in enumerate(ele_pair):
            if idx != i and num[idx] != num[i]:
                break
        if idx == i:
            return int(num)
        num = num[:i] + num[idx] + num[i+1:idx] + num[i] + num[idx+1:]
        return int(num)

# better solution -- O(N)
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int, str(num)))
        ele_idx = collections.defaultdict(int)
        for i in range(len(num)):
            ele_idx[num[i]] = i
        for idx, ele in enumerate(num):
            for j in range(9, ele, -1):
                if idx < ele_idx[j]:
                    num[idx], num[ele_idx[j]] = num[ele_idx[j]], num[idx]
                    return int("".join(map(str, num)))
        return int("".join(map(str, num)))
    
                    
        
    