# tc: o(n), sc: o(n)
class QueueTwoStacks(object):
    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.stack_one = deque()
        self.stack_two = deque()

    def enqueue(self, item):
        self.stack_one.append(item)

    def dequeue(self):
        if len(self.stack_two) == 0:
            if len(self.stack_one) == 0:
                raise Exception('Queue is empty')

            while len(self.stack_one) != 0:
                first_element_one = self.stack_one.pop()
                self.stack_two.append(first_element_one)
            
        first_element_two = self.stack_two.pop()
        return first_element_two 
