"""
LC621 task scheduler

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
        