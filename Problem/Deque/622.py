class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self._max = k
        self._queue = [None] * k
        self._front = 0
        self._rear = -1
        self._count = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        #if self._count >= self._max:
        if self.isFull():
            return False
        self._rear  = (self._rear + 1) % self._max
        self._queue[self._rear] = value
        self._count += 1
        return True
        
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty() is True:
            return False
        
        self._front = (self._front + 1) % self._max
        #self._queue[self._front] = None
        self._count -= 1
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty() == True:
            return -1
        return self._queue[self._front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty() == True:
            return -1
        return self._queue[self._rear]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self._count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self._count == self._max
