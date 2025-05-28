import unittest
from support_ticket import Queue, Stack, Ticket

class TestSupportTicketSystem(unittest.TestCase):
    def test_ticket_flow(self):
        q = Queue()
        s = Stack()
        ticket = Ticket(1, "Internet not working")
        q.enqueue(ticket)
        t = q.dequeue()
        s.push(t)
        self.assertEqual(s.pop().issue_description, "Internet not working")

if __name__ == "__main__":
    unittest.main()