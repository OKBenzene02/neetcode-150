class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = 99999999

    def push(self, val: int) -> None:
        if not self.stack:
            self.minimum = val
            self.stack.append(val)
        else:
            if val > self.minimum: self.stack.append(val)
            else:
                self.stack.append(2 * val - self.minimum)
                self.minimum = val

    def pop(self) -> None:
        if not self.stack: return
        else:
            top = self.stack.pop()
            if top < self.minimum:
                 self.minimum = 2 * self.minimum - top

    def top(self) -> int:
        top = self.stack[-1]
        if top < self.minimum: return self.minimum
        return top


    def getMin(self) -> int:
        return self.minimum
        
