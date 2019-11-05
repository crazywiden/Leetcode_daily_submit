"""
LC1215. Stepping Numbers
A Stepping Number is an integer such that all of its adjacent digits have an absolute difference of exactly 1. For example, 321 is a Stepping Number while 421 is not.

Given two integers low and high, find and return a sorted list of all the Stepping Numbers in the range [low, high] inclusive.

 

Example 1:

Input: low = 0, high = 21
Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]
 

Constraints:

0 <= low <= high <= 2 * 10^9
"""


# bianry search
# Runtime: 304 ms, faster than 54.02% of Python3 online submissions for Stepping Numbers.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Stepping Numbers.
class Solution:
    def countSteppingNumbers(self, low: int, high: int):
        # first generate all stepping number
        # use binary search to find index of low and high
        all_num = list(range(10))
        new_num = list(range(1, 10))
        is_reach = False # if we have covered the interval contains [low, high]
        while not is_reach:
            if high < new_num[-1]:
                break
            tmp_num = []
            for i in range(len(new_num)):
                digits = str(new_num[i])
                if digits[-1] != "0":
                    smaller = int(digits+str(int(digits[-1]) - 1))
                    tmp_num.append(smaller)

                if digits[-1] != "9":
                    larger = int(digits+str(int(digits[-1]) + 1))
                    tmp_num.append(larger)

                if tmp_num[-1] >= high:
                    is_reach = True
                    break
            new_num = tmp_num.copy()
            all_num.extend(new_num.copy())
                    

        low_idx = self.binary_search(all_num, 0, len(all_num)-1, low)
        high_idx = self.binary_search(all_num, 0, len(all_num)-1, high)
        
        if all_num[low_idx] < low:
            low_idx += 1
        if all_num[low_idx] > high:
            high_idx -= 1
        return all_num[low_idx:high_idx+1]
    
    def binary_search(self, search_list, start, end, target):
        if start == end:
            return start
        if end - start == 1:
            if search_list[start] <= target and search_list[end] > target:
                return start
            else:
                return end

        mid = (start + end) // 2

        if search_list[mid] == target:
            return mid

        if search_list[mid] > target:
            return self.binary_search(search_list, start, mid-1, target)
        if search_list[mid] < target:
            return self.binary_search(search_list, mid, end, target)



# method 2:
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        res=[]
        if low==0:
            res.append(0)
        q=[i for i in range(1,10)]
        while q:
            newq=[]
            for i in q:
                if low<=i<=high:
                    res.append(i)
                v=i%10
                if v-1>=0 and i*10+v-1<=high:
                    newq.append(i*10+v-1)
                if v+1<10 and i*10+v+1<=high:
                    newq.append(i*10+v+1)
            q=newq
        return res


