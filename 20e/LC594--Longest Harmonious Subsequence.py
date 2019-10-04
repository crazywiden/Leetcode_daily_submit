'''
Time complexity: O(n),416 ms, 90.43%
Space complexity: O(n),15.8 MB, 5.55%
'''
#method1: iteration+hashmap
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(set(nums)) == 1:
            return 0

        numdict = dict()
        for i in nums:
            if i in numdict:
                numdict[i] = numdict[i] + 1
            else:
                numdict[i] = 1
        print(numdict)

        max_d = 0
        for i in numdict.keys():
            j = i + 1
            k = i - 1
            if j in numdict:
                max_d = max(numdict[i] + numdict[j], max_d)
            if k in numdict:
                max_d = max(numdict[i] + numdict[k], max_d)
        return max_d