class MyQueue:

    def __init__(self):
        self.front = []  # dequeue(pop)
        self.back = []   # enqueue(push)

    def push(self, x: int) -> None:
        self.back.append(x)

    def pop(self) -> int:
        self.move()
        return self.front.pop()

    def peek(self) -> int:
        self.move()
        return self.front[-1]
        
    def empty(self) -> bool:
        return not self.front and not self.back

    def move(self) -> None:
        if not self.front:
            while self.back:
                self.front.append(self.back.pop())
