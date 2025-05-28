class Reservation:
    def __init__(self, user_name, book_title):
        self.user_name = user_name
        self.book_title = book_title

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def peek(self):
        return self.items[0] if self.items else None