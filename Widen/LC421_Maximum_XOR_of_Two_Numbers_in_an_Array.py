"""
LC421. Maximum XOR of Two Numbers in an Array
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""

# trie act as a hash map here
# the key idea should be:
# if x is the max result we can get, then there must be two numbers a, b s.t. a ^ b == x
# so there must be a ^ x == b
# notice the maximum result we can get is "all the digits are 1", so for each number, we try every digit
# if there exists such number that can make that digit equals to 1, then that digit will be one
# Runtime: 1096 ms, faster than 17.77% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
# Memory Usage: 151.3 MB, less than 100.00% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
def num2bin(num):
    bin_num = bin(num)[2:]
    str_num = "0" * (31-len(bin_num)) + bin_num
    return str_num

class TrieNode:
    def __init__(self):
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, num):
        node = self.root
        str_num = num2bin(num)
        for n in str_num:
            if n not in node.children:
                node.children[n] = TrieNode()
            node = node.children[n]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        TrieTree = Trie()
        for num in nums:
            TrieTree.insert(num)
        
        res = 0
        for num in nums:
            tmp_max = ""
            str_num = num2bin(num)
            node = TrieTree.root
            for digit in str_num:
                xor_with_one = "1" if digit == "0" else "0"
                if xor_with_one in node.children:
                    tmp_max += "1"
                    node = node.children[xor_with_one]
                else:
                    tmp_max += "0"
                    node = node.children[digit]
            res = max(int(tmp_max, 2), res)
        return res
            
        