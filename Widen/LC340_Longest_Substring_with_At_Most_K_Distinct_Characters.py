"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""



# in fact not that hard, pretty straight foward implementation
# Runtime: 120 ms, faster than 18.97% of Python online submissions for Longest Substring with At Most K Distinct Characters.
# Memory Usage: 14.4 MB, less than 33.33% of Python online submissions for Longest Substring with At Most K Distinct Characters.
import collections
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # first generate a aggregated list
        if len(s) == 0 or k <= 0:
            return 0
        
        agg_str, agg_cnt = [s[0]], [1]
        for i in range(1, len(s)):
            if s[i] == agg_str[-1]:
                agg_cnt[-1] += 1
            else:
                agg_str.append(s[i])
                agg_cnt.append(1)
                
        if len(agg_cnt) <= k:
            return len(s)
        print(agg_cnt, agg_str)
        memo = collections.defaultdict(int) # different type of strings in given interval
        max_cnt, cnt = 0, 0# save the length of maximum substring that satisfies condition
        start = 0  # start index in agg_str of current interval

        for i in range(len(agg_cnt)):
            # print(cnt, max_cnt)
            if agg_str[i] in memo:
                cnt += agg_cnt[i]
                memo[agg_str[i]] += agg_cnt[i]
                continue
            while len(memo) >= k:
                max_cnt = max(cnt, max_cnt)
                memo[agg_str[start]] -= agg_cnt[start]
                cnt -= agg_cnt[start]
                if memo[agg_str[start]] == 0:
                    memo.pop(agg_str[start])
                start += 1
                    
            if agg_str[i] not in memo:
                cnt += agg_cnt[i]
                memo[agg_str[i]] = agg_cnt[i]
        max_cnt = max(cnt, max_cnt)
        return max_cnt
                



# method 2: don't use default hash, use self-construct hash using index as key
# Runtime: 68 ms, faster than 56.60% of Python online submissions for Longest Substring with At Most K Distinct Characters.
# Memory Usage: 12.2 MB, less than 100.00% of Python online submissions for Longest Substring with At Most K Distinct Characters.
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest, start, distinct_count, visited = 0, 0, 0, [0 for _ in xrange(256)]
        for i, char in enumerate(s):
            if visited[ord(char)] == 0:
                distinct_count += 1
            visited[ord(char)] += 1
             
            while distinct_count > k:
                visited[ord(s[start])] -= 1
                if visited[ord(s[start])] == 0:
                    distinct_count -= 1
                start += 1
   
            longest = max(longest, i - start + 1)
        return longest