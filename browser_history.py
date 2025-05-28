class Stack:
    def __init__(self):
        self.items = []

    def push(self, url):
        self.items.append(url)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None