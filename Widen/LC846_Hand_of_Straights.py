"""
846. Hand of Straights
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
"""

# use hashmap
# time complexity -- O(kN)
# Runtime: 340 ms, faster than 32.31% of Python3 online submissions for Hand of Straights.
# Memory Usage: 15.5 MB, less than 50.00% of Python3 online submissions for Hand of Straights.
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0:
            return False
        freq = collections.Counter(hand)

        for val in sorted(hand):
            if freq[val] == 0:
                continue
            tmp = val
            for i in range(W):
                if tmp not in freq:
                    return False
                if freq[tmp] == 0:
                    return False
                freq[tmp] -= 1
                tmp += 1
        return True

# brutal force
# time complexity -- O(n^2) 
# Runtime: 3560 ms, faster than 5.04% of Python3 online submissions for Hand of Straights.
# Memory Usage: 15.1 MB, less than 50.00% of Python3 online submissions for Hand of Straights.
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0:
            return False
        visited = [False for _ in range(n)]
        hand = sorted(hand)
        for i in range(n):
            if visited[i]:
                continue
            straights = [hand[i]]
            visited[i] = True
            for j in range(n):
                if visited[j]:
                    continue
                if len(straights) >= W:
                    break
                if hand[j] - straights[-1] == 1:
                    straights.append(hand[j])
                    visited[j] = True
            if len(straights) < W:
                return False
        return True
    
                
        