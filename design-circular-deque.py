class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = [-1] * k
        self.front = 0
        self.rear = 0
        self.capacity = k
        self.size = 0
        
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.deque[self.front] = value
        else:
            self.front = (self.front - 1) % self.capacity
            self.deque[self.front] = value
        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            key = self.rear
            self.deque[key] = value
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.deque[self.rear] = value
        self.size += 1
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.deque[self.front] = -1
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.isEmpty():
            self.rear = self.front
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.deque[self.rear] = -1
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        if self.isEmpty():
            self.front = self.rear
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.deque[self.front]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.deque[self.rear]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.capacity
        

