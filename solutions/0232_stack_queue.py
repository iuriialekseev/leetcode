# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity?
# In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.move(self.pop_stack, self.push_stack)
        self.push_stack.append(x)

    def pop(self) -> int:
        self.move(self.push_stack, self.pop_stack)
        return self.pop_stack.pop()

    def peek(self) -> int:
        self.move(self.push_stack, self.pop_stack)
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return not self.push_stack and not self.pop_stack

    def move(self, out, to) -> None:
        while out:
            to.append(out.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
