import unittest
from containers.stack import Stack

class TestStackMethods(unittest.TestCase):
    def test_push(self):
        newStack = stack()
        newStack.push(1)
        self.assertEqual(newStack, [1])

    def test_pop(self):
        newStack = stack([1,2,3,4])
        popped = newStack.pop()
        self.assertEqual(popped, 4)

    def test_pop_from_empty_stack(self):
        newStack = stack()
        popped = newStack.pop()
        self.assertEqual(popped, None)

    def test_peek(self):
        newStack = stack([1,2,3,4])
        self.assertEqual(newStack.peek(), 4)

    def test_peek_empty_stack(self):
        newStack = stack()
        self.assertEqual(newStack.peek(), None)

    def test_clear(self):
        newStack = stack([1,2,3,4,5])
        newStack.clear()
        self.assertEqual(newStack, [])


if __name__ == "__main__":
    unittest.main()