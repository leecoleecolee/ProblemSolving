'''
나는 배열을 이용해서 풀었는데,
이중 연결리스트로도 나중에 풀어보자.
'''

# --- 배열을 이용한 풀이
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.array = [None] * k
        self.size = k
        self.front = 0
        self.end = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.front = (self.front - 1) % self.size
        self.array[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        self.end = (self.end + 1) % self.size
        self.array[self.end - 1] = value
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.array[self.front] = None
        self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.array[self.end - 1] = None
        self.end = (self.end - 1) % self.size
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.array[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.array[self.end - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.end and self.array[self.front] is None

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.front == self.end and self.array[self.front] is not None


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()