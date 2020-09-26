class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev, self.next = prev, next

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head, self.tail = ListNode(None), ListNode(None)
        self.max = k
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _add(self, node: ListNode, new: ListNode):
        if self.size == self.max:
            return False
        self.size += 1
        temp = node.next
        node.next = temp.prev = new
        return True
    
    def _delete(self, node: ListNode):
        if self.size == 0:
            return False
        self.size -= 1
        temp = node.next.next
        node.next, temp.prev = temp, node
        return True
        
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        return self._add(self.head, ListNode(value, self.head, self.head.next))
        
    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        return self._add(self.tail.prev, ListNode(value, self.tail.prev, self.tail))       
        
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        return self._delete(self.head)

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        return self._delete(self.tail.prev.prev)

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.size > 0:
            return self.head.next.val
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.size > 0:
            return self.tail.prev.val
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.max
