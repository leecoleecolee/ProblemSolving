import collections

'''
# ---
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # tmp = collections.deque()
        # while self.queue:
        #     elem = self.queue.popleft()
        #     if not self.queue:
        #         self.queue = tmp # 되나?
        #         return elem
        #     tmp.append(elem)
        length = len(self.queue)
        for i in range(length):
            elem = self.queue.popleft()
            if i == length - 1:
                return elem
            self.queue.append(elem)

    def top(self) -> int:
        """
        Get the top element.
        """
        # tmp = collections.deque()
        # while self.queue:
        #     elem = self.queue.popleft()
        #     if not self.queue:
        #         tmp.append(elem)
        #         self.queue = tmp # 되나?
        #         return elem
        #     tmp.append(elem)

        length = len(self.queue)
        for i in range(length):
            elem = self.queue.popleft()
            if i == length - 1:
                self.queue.append(elem)
                return elem
            self.queue.append(elem)

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        # if self.queue:
        #     return False
        # else:
        #     return True
        # return queue # 한번에 이 문장으로 어떻게 하지?

        return len(self.queue) == 0
'''

# --- push할 때 먼저 넣은 것을 뒤로 정렬하는 방식
class MyStack:

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        # return len(self.queue) == 0
        return not self.queue

# ---
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

print (param_2, param_3, param_4)