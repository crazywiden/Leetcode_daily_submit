"""
LC621 task scheduler
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
"""

# Runtime: 440 ms, faster than 65.87% of Python3 online submissions for Task Scheduler.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Task Scheduler.
from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_freq = 0
        max_freq_task = 0
        freq = defaultdict(int)
        for letter in tasks:
            freq[letter] += 1
            if freq[letter] == max_freq:
                max_freq_task += 1
            elif max_freq < freq[letter]:
                max_freq = freq[letter]
                max_freq_task = 1
        
        avaliable_slot = (n - max_freq_task + 1) * (max_freq - 1)
        avaliable_task = len(tasks) - max_freq * max_freq_task
        idle = max(0, avaliable_slot - avaliable_task)
        return len(tasks) + idle

# faster version
# Runtime: 404 ms, faster than 92.71% of Python3 online submissions for Task Scheduler.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Task Scheduler.
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_freq = 0
        num_task_max_freq = 0
        all_freq = collections.Counter(tasks)
        for letter, freq in all_freq.items():
            if max_freq == freq:
                num_task_max_freq += 1
            elif max_freq < freq:
                max_freq = freq
                num_task_max_freq = 1
        
        avaliable_slot = (n - num_task_max_freq + 1) * (max_freq - 1)
        avaliable_task = len(tasks) - num_task_max_freq * max_freq
        idle = max(0, avaliable_slot - avaliable_task)
        return len(tasks) + idle
        