"""
1199. Minimum Time to Build Blocks
You are given a list of blocks, where blocks[i] = t means that the i-th block needs t units of time to be built. A block can only be built by exactly one worker.

A worker can either split into two workers (number of workers increases by one) or build a block then go home. Both decisions cost some time.

The time cost of spliting one worker into two workers is given as an integer split. Note that if two workers split at the same time, they split in parallel so the cost would be split.

Output the minimum time needed to build all blocks.

Initially, there is only one worker.

 

Example 1:

Input: blocks = [1], split = 1
Output: 1
Explanation: We use 1 worker to build 1 block in 1 time unit.
Example 2:

Input: blocks = [1,2], split = 5
Output: 7
Explanation: We split the worker into 2 workers in 5 time units then assign each of them to a block so the cost is 5 + max(1, 2) = 7.
Example 3:

Input: blocks = [1,2,3], split = 1
Output: 4
Explanation: Split 1 worker into 2, then assign the first worker to the last block and split the second worker into 2.
Then, use the two unassigned workers to build the first two blocks.
The cost is 1 + max(3, 1 + max(1, 2)) = 4.
"""



# tutorial: https://nagato1208.github.io/2019/09/21/leetcode-1199-Minimum-Time-to-Build-Blocks/
# tutorial: https://leetcode-cn.com/circle/article/UH0fwx/
# such a brilliant idea to use Huffman encoding!!
# time complexity -- O(Nlog N)
# Runtime: 124 ms, faster than 31.25% of Python3 online submissions for Minimum Time to Build Blocks.
# Memory Usage: 14 MB, less than 60.00% of Python3 online submissions for Minimum Time to Build Blocks.
class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heap = []
        for ele in blocks:
            heapq.heappush(heap, ele)
        while len(heap) > 1:
            ele1 = heapq.heappop(heap)
            ele2 = heapq.heappop(heap)
            heapq.heappush(heap, split + max(ele1, ele2))
        return heap[0]

# another follow up: what if there is no limit to a worker's maximum number of project?
# I AM THE BEST
class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heap = []
        for ele in blocks:
            heapq.heappush(heap, ele)
        while len(heap) > 1:
            ele1 = heapq.heappop(heap)
            ele2 = heapq.heappop(heap)
            min_ele = min(ele1, ele2)
            heapq.heappush(heap, min(split, min_ele) + max(ele1, ele2))
        return heap[0]



            