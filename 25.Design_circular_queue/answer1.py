class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if self.q[self.front] is None else self.q[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        # if self.q[self.front] is None and self.q[self.rear] is None:
        #     return True
        # else:
        #     return False
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        # if self.rear + 1 == self.front:
        #     return True
        # return False
        return self.front == self.rear and self.q[self.front] is not None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
