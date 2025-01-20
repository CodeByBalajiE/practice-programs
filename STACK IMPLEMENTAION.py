# Stack implementation using a list
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# Example Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(f"Top element: {s.peek()}")
print(f"Popped element: {s.pop()}")
print(f"Is stack empty? {s.is_empty()}")
