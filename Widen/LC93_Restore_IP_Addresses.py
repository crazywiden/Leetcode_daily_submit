"""
LC93. Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

# backtracking
# Runtime: 32 ms, faster than 66.20% of Python3 online submissions for Restore IP Addresses.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Restore IP Addresses.
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 and len(s) > 12:
            return []
        
        res = []
        self.dfs(res, [], s, 0)
        return res
    
    def dfs(self, res, tmp, s, level):
        if level > 4:
            return 
        if len(s) == 0 and level == 4:
            res.append(".".join(tmp))
            return 
        
        for k in range(1, 4):
            if k > len(s):
                continue
            address = s[:k]
            if not self.valid(address):
                continue
            tmp.append(address)
            level += 1
            self.dfs(res, tmp, s[k:], level)
            # print(s,tmp)
            level -= 1
            tmp.pop()
        
    def valid(self, address):
        if address[0] == "0":
            return len(address) == 1
        return 1 <= int(address) <= 255
    
    
        