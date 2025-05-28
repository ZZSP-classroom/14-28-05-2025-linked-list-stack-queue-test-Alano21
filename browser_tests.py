import unittest
from browser_history import Stack

class TestBrowserHistory(unittest.TestCase):
    def test_stack_navigation(self):
        s = Stack()
        s.push("xhumster.com")
        s.push("pornhub.com")
        self.assertEqual(s.pop(), "pornhub.com")
        self.assertEqual(s.peek(), "xhumster.com")

if __name__ == "__main__":
    unittest.main()