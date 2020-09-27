class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        tmp = []
        leng = len(self.stack)
        for _ in range(leng - 1):
            tmp.append(self.stack.pop())
        ret = self.stack.pop()
        while tmp:
            self.stack.append(tmp.pop())
        return ret
        

    def peek(self) -> int:
        tmp = []
        leng = len(self.stack)
        for _ in range(leng - 1):
            tmp.append(self.stack.pop())
        ret = self.stack[-1]
        while tmp:
            self.stack.append(tmp.pop())
        return ret

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()