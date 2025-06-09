# Defining a Stack class
class Stack:
    def __init__(self):
        self.stack = []  # Start with an empty list
    def push(self, item):
        # Add item to the top of the stack
        self.stack.append(item)
    def pop(self):
        # Remove and return the top item
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
    def peek(self):
        # Show the top item without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0
# Using the stack
my_stack = Stack()
# Pushing numbers
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)
# Peeking at the top
print("Top of the stack:", my_stack.peek())  # Output: 15
# Removing the top element
print("Popped item:", my_stack.pop())        # Output: 15
# Top after popping
print("New top:", my_stack.peek())           # Output: 10
