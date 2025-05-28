class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song

    def remove_song(self):
        if self.head:
            removed = self.head
            self.head = self.head.next
            return removed
        return None

    def get_next_song(self):
        return self.head