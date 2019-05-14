# Create:
# Read: size, peek
# Update: push
# Delete: pop, clear

import unittest
from containers.Queue import Queue

class TestQueueMethods(unittest.TestMethod):
    def test_constructor(self):
        try:
            q = Queue()
            print('TEST CONSTRUCTOR: PASS')
        except:
            print('TEST CONSTRUCTOR: FAIL')

    def test_size(self):
        q = Queue()
        self.assertEqual(q.size(), 0)

    def test_push(self):
        q = Queue()
        self.assertEqual(q.size(), 0)
        q.push(1)
        q.push(2)
        self.assertEqual(q.size(), 2)

    def test_type_checking(self):
        q = Queue()
        q.push('a')
        try:
            q.push(1)
            print('TEST TYPE CHECK: FAIL')
        except:
            print('TEST TYPE CHECK: PASS')

    def test_pop(sef):
        q = Queue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.pop(), 2)
        self.assertEqual(q.pop(), None)

    def test_peek(sef):
        q = Queue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.peek(), 1)
        q.pop()
        self.assertEqual(q.peek(), 2)
        q.pop()
        self.assertEqual(q.peek(), None)

    def test_clear(self):
        q = Queue()
        q.push(1)
        q.push(2)
        q.push(3)
        q.clear()
        self.assertEqual(q.size(), 0)