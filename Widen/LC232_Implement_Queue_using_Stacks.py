"""
232. Implement Queue using Stacks
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
"""

# use the idea of two stacks
# to achieve amortized time complexity as O(1)
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main_stack = []
        self.queue_stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.main_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.queue_stack) != 0:
            return self.queue_stack.pop()
        while len(self.main_stack) > 0:
            ele = self.main_stack.pop()
            self.queue_stack.append(ele)
        return self.queue_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.queue_stack) != 0:
            return self.queue_stack[-1]
        while len(self.main_stack) > 0:
            ele = self.main_stack.pop()
            self.queue_stack.append(ele)
        return self.queue_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.main_stack) == 0 and len(self.queue_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()