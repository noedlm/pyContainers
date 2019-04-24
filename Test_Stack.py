import unittest
from containers.stack import stack

class TestStackMethods(unittest.TestCase):
    def test_push(self):
        newStack = stack()
        newStack.push(1)
        self.assertEqual(newStack, [1])

    def test_pop(self):
        newStack = stack([1,2,3,4])
        popped = newStack.pop()
        self.assertEqual(popped, 4)

    def test_clear(self):
        newStack = stack([1,2,3,4,5])
        newStack.clear()
        self.assertEqual(newStack, [])

