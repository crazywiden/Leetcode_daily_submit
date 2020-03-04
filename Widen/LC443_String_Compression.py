"""
443. String Compression
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
"""
# two pointers
# Runtime: 52 ms, faster than 94.08% of Python3 online submissions for String Compression.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for String Compression.
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        left, right = 0, 0
        curr = 0
        while left < n:
            left = right
            if left >= n:
                break
            while right < n and chars[left] == chars[right]:
                right += 1
            chars[curr] = chars[left]
            curr += 1
            if right-left == 1:
                continue
            for c in str(right-left):
                chars[curr] = c
                curr += 1
            
        return curr