"""
465. Optimal Account Balancing
A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

Note:

A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
Example 1:

Input:
[[0,1,10], [2,0,5]]

Output:
2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
Example 2:

Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.
"""


# back-tracking of pre-processed data
# tutorial: https://www.cnblogs.com/grandyang/p/6108158.html
# Runtime: 2172 ms, faster than 20.15% of Python3 online submissions for Optimal Account Balancing.
# Memory Usage: 13.7 MB, less than 25.00% of Python3 online submissions for Optimal Account Balancing.
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = collections.defaultdict(int)
        for out_person, in_person, amount in transactions:
            balance[out_person] -= amount
            balance[in_person] += amount
        res = len(balance)
        deposit = []
        for key, val in balance.items():
            if val != 0:
                deposit.append(val)
        res = self.dfs(deposit, 0, 0, res)
        return res
    
    def dfs(self, deposit, start, cnt, res):
        while start < len(deposit) and deposit[start] == 0:
            start += 1
        if start == len(deposit):
            return min(cnt, res)
        for i in range(start+1, len(deposit)):
            if deposit[i] * deposit[start] < 0:
                deposit[i] += deposit[start]
                tmp = self.dfs(deposit, start+1, cnt+1, res)
                res = min(res, tmp)
                deposit[i] -= deposit[start]
        return res
    
            
        
        