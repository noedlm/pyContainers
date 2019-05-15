'''
Create:
Read: <T> peek (1), int size (1)
Update: void push (1)
Delete: <T> pop (1), void clear (1)
'''
import unittest
from containers.stack import Stack

class TestStackMethods(unittest.TestCase):
    def test_initialize_empty_stack(self):
        try:
            newStack = Stack()
            print("test_initialize_empty_stack: PASS")
        except:
            print("test_initialize_empty_stack: FAIL")

    def test_size(self):
        newStack = Stack()
        self.assertFalse(newStack.size())

    def test_is_empty(self):
        newStack = Stack()
        self.assertTrue(newStack.is_empty())

    def test_push(self):
        newStack = Stack()
        newStack.push(1)
        self.assertEqual(newStack.size(), 1)

    def test_pop(self):
        newStack = Stack([1,2,3,4])
        popped = newStack.pop()
        self.assertEqual(popped, 4)
        self.assertEqual(newStack.size(), 3)

    def test_pop_from_empty_stack(self):
        newStack = Stack()
        popped = newStack.pop()
        self.assertEqual(popped, None)

    def test_peek(self):
        newStack = Stack([1,2,3,4])
        self.assertEqual(newStack.peek(), 4)

    def test_peek_empty_stack(self):
        newStack = Stack()
        self.assertEqual(newStack.peek(), None)

    def test_clear(self):
        newStack = Stack([1,2,3,4,5])
        newStack.clear()
        self.assertEqual(newStack.size(), 0)


if __name__ == "__main__":
    unittest.main()