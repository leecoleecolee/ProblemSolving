class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = [None] * k
        self.front, self.rear = -1, -1
        self.max = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.front == -1:
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.max - 1
        else:
            self.front -= 1
        self.deque[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max
        self.deque[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            print("front: ", self.front)
            print("rear: ", self.rear)
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.max - 1
        else:
            self.rear = self.rear - 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return - 1
        return self.deque[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self.front == 0 and (self.rear == self.max -1):
            return True
        elif self.front == self.rear + 1:
            return True
        return False

