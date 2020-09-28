class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        tmp = []
        for _ in range(len(self.stack) - 1):
            tmp.append(self.stack.pop())
        ret = self.stack.pop()
        while tmp:
            self.stack.append(tmp.pop())
        # 책에서는 tmp에 옮겼다가 다시 stack으로 옮기지 않고, 멤버변수로 유지함. 훨씬 효율적.
        return ret

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        # return len(self.stack) == 0
        return not self.stack