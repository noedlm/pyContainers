# Create:
# Read: size, is_empty, peek_front, peek_back
# Update: pushFront, pushBack
# Delete: pop_front, pop_back

import unittest
from containers.Deque import Deque

class TestDequeListMethods(unittest.TestCase):
    def test_constructor(self):
        # default constructor
        try:
            dequeDefault = Deque()
            print("test_constructor: PASS default")
        except:
            print("test_constructor: FAIL default")

        # constructor with data
        try:
            dequeData = Deque([1, 2, 3])
            print("test_constructor: PASS constructor with data")
        except:
            print("test_constructor: FAIL constructor with data")

    def test_size(self):
        # empty
        dequeEmpty = Deque()
        self.assertEquals(dequeEmpty.size(), 0)

        # not empty
        dequeNotEmpty = Deque([1, 2, 3])
        self.assertEquals(dequeNotEmpty.size(), 3)

    def test_is_empty(self):
        # empty
        dequeEmpty = Deque()
        self.assertTrue(dequeEmpty.is_empty())

        # not empty
        dequeNotEmpty = Deque([1])
        self.assertFalse(dequeNotEmpty.is_empty())

    def test_peek_front(self):
        # empty
        dequeEmpty = Deque()
        try:
            dequeEmpty.peek_front()
            print("test_peek_front: FAIL empty")
        except:
            print("test_peek_front: PASS empty")

        # not empty
        dequeNotEmpty = Deque([1, 2])
        self.assertEquals(dequeNotEmpty.peek_front(), 1)

    def test_peek_back(self):
        # empty
        dequeEmpty = Deque()
        try:
            dequeEmpty.peek_back()
            print("test_peek_back: FAIL empty")
        except:
            print("test_peek_back: PASS empty")

        # not empty
        dequeNotEmpty = Deque([1, 2])
        self.assertEquals(dequeNotEmpty.peek_back(), 2)

    def test_pushFront(self):
        deque = Deque()

        # empty
        deque.pushFront("front")
        self.assertEquals(deque.peek_back(), "front")
        
        # not empty
        deque.pushFront("new front")
        self.assertEquals(deque.peek_front(), "new front")

        # different type
        self.assertRaises(TypeError, deque.pushFront(0))

    def test_pushBack(self):
        deque = Deque()
        # empty
        deque.pushBack("back")
        self.assertEquals(deque.peek_front(), "back")

        # not empty
        deque.pushBack("new back")
        self.assertEquals(deque.peek_back(), "new back")

        # different type
        self.assertRaises(TypeError, deque.pushBack(0))

    def test_pop_front(self):
        # empty
        dequeEmpty = Deque()
        try:
            dequeEmpty.pop_front()
            print("test_pop_front: FAIL empty")
        except:
            print("test_pop_front: PASS empty")
        
        # not empty
        dequeNotEmpty = Deque([0, 1, 2])
        dequeNotEmpty.pop_front()
        self.assertEquals(dequeNotEmpty.size(), 2)
        self.assertEquals(dequeNotEmpty.peek_front(), 1)
        self.assertEquals(dequeNotEmpty.peek_back(), 2)

    def test_pop_back(self):
        # empty
        dequeEmpty = Deque()
        try:
            dequeEmpty.pop_back()
            print("test_pop_back: FAIL empty")
        except:
            print("test_pop_back: PASS empty")
        
        # not empty
        dequeNotEmpty = Deque([0, 1, 2])
        dequeNotEmpty.pop_back()
        self.assertEquals(dequeNotEmpty.size(), 2)
        self.assertEquals(dequeNotEmpty.peek_front(), 0)
        self.assertEquals(dequeNotEmpty.peek_back(), 1)
