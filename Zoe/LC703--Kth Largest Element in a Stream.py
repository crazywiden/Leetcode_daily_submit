
'''
Time complexity: 1796 ms, 11.47%, O(n)
Space complexity: 17.5 MB, 5.63%
'''
#method1: using sorted-list
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort(reverse = True)
        self.nums = self.nums[:self.k]

    def add(self, val: int) -> int:
        if len(self.nums)>=self.k:
            if val > self.nums[self.k-1]:
                self.nums[self.k-1] = val
        else:
            self.nums.append(val)
        self.nums.sort(reverse = True)
        return self.nums[self.k-1]


'''
Time complexity: 120 ms, 87.19%, O(n)
Space complexity: 17.9 MB, 5.63%
'''
#method2: using heap, comparing the smallest one in largest K elements with the entried value

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pool = heapq.nlargest(k, nums)
        self.pool = heapq.nsmallest(k, self.pool)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]