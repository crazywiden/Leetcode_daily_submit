"""
LC822 -- Card Flip Game
On a table are N cards, with a positive integer printed on the front and back of each card (possibly different).

We flip any number of cards, and after we choose one card. 

If the number X on the back of the chosen card is not on the front of any card, then this number X is good.

What is the smallest number that is good?  If no number is good, output 0.

Here, fronts[i] and backs[i] represent the number on the front and back of card i. 

A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.

Example:

Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so 2 is good.
"""
# method 1
# Runtime: 152 ms, faster than 20.97% of Python3 online submissions for Card Flipping Game.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Card Flipping Game.

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        all_numbers = fronts + backs
        all_numbers.sort()
        front_dict = {i:set() for i in fronts}
        back_dict = {i:set() for i in backs}
        for i in range(len(fronts)):
            front_item = fronts[i]
            back_item = backs[i]
            front_dict[front_item].add(i)
            back_dict[back_item].add(i)
            
        for num in all_numbers:
            if num in front_dict and num in back_dict:
                front_idx = front_dict[num]
                back_idx = back_dict[num]
                if bool(front_idx & back_idx):
                    continue
                return num
            return num
        return 0
           

# method 2
# same algorithm but way faster and neat!!
# programming is a long way to go
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        
        # solution 1: lee215
        # runtime:
        """
        If fronts[i] == backs[i], it means that fronts[i] is sure to appear on the table, no matter how we flap this card.
        In case that fronts[i] and backs[i] are same, fronts[i] become impossible to be good number, so I add it to a set same.

        If fronts[i] != backs[i], we can always hide either number by flapping it to back.

        Then loop on all numbers and return the minimum.
        """
        same = {x for x, y in zip(fronts, backs) if x == y}
        
        return min([i for i in fronts + backs if i not in same] or [0])

