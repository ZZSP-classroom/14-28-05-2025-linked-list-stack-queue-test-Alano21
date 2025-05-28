import unittest
from library_reservation import Queue, Reservation

class TestLibraryReservation(unittest.TestCase):
    def test_queue_order(self):
        q = Queue()
        q.enqueue(Reservation("example1", "2000"))
        q.enqueue(Reservation("example1", "example1"))
        self.assertEqual(q.peek().user_name, "example1")

    def test_dequeue(self):
        q = Queue()
        q.enqueue(Reservation("example1", "2000"))
        q.dequeue()
        self.assertIsNone(q.peek())
if __name__ == "__main__":
    unittest.main()