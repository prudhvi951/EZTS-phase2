class MyQueue:

    def __init__(self):
        self.k = []

    def push(self, x: int) -> None:
        self.x = x
        self.k.append(self.x)

    def pop(self) -> int:
        return self.k.pop(0)

    def peek(self) -> int:
        return self.k[0]

    def empty(self) -> bool:
        if len(self.k) == 0:
            return True
        else:
            return False   
