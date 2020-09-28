# --- 배열을 이용한 풀이
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.array = [None] * k # 배열 초기화
        self.size = k
        self.front = 0
        self.end = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.array[self.end] = value
        self.end = (self.end + 1) % self.size
        return True


    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.array[self.front] = None
        self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.array[self.front]
        # return -1 if self.isEmpty() else self.array[self.front] # 삼항연산자로도 가능. 그러나 가독성이 좋나?

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.array[self.end - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        # return self.front == self.end and self.array[self.front] is None
        return self.array[self.front] is None # 생각해보면 isEmpty는 이렇게 해도 될 듯.

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.front == self.end and self.array[self.front] is not None
        # return self.array[self.front] is not None # isFull은 당연히 검사해야하고.


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()