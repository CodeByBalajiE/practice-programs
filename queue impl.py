# Class to represent a queue
class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty queue

    def enqueue(self, item):
        self.queue.append(item)  # Add the item to the end of the queue

    def dequeue(self):
        if len(self.queue) == 0:  # Check if the queue is empty
            return "Queue is empty"
        return self.queue.pop(0)  # Remove and return the front item

    def peek(self):
        if len(self.queue) == 0:  # Check if the queue is empty
            return "Queue is empty"
        return self.queue[0]  # Return the front item without removing it

    def is_empty(self):
        return len(self.queue) == 0  # Check if the queue is empty

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(f"Front element: {q.peek()}")
print(f"Dequeued element: {q.dequeue()}")
print(f"Is queue empty? {q.is_empty()}")
