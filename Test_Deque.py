# Create:
# Read: size, isEmpty, peekFront, peekBack
# Update: pushFront, pushBack
# Delete: popFront, popBack

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

    def test_isEmpty(self):
        # empty
        dequeEmpty = Deque()
        self.assertTrue(dequeEmpty.isEmpty())

        # not empty
        dequeNotEmpty = Deque([1])
        self.assertFalse(dequeNotEmpty.isEmpty())

    def test_peekFront(self):
        # empty
        dequeEmpty = Deque()
        try:
            dequeEmpty.peekFront()
            print("test_peekFront: FAIL empty")
        except:
            print("test_peekFront: PASS empty")

        # not empty
        dequeNotEmpty = Deque([1, 2])
        self.assertEquals(dequeNotEmpty.peekFront(), 1)

    def test_peekBack(self):
        # empty
        dequeEmpty = Deque()
        try:
            dequeEmpty.peekBack()
            print("test_peekBack: FAIL empty")
        except:
            print("test_peekBack: PASS empty")

        # not empty
        dequeNotEmpty = Deque([1, 2])
        self.assertEquals(dequeNotEmpty.peekBack(), 2)

    def test_pushFront(self):
        deque = Deque()

        # empty
        deque.pushFront("front")
        self.assertEquals(deque.peekBack(), "front")
        
        # not empty
        deque.pushFront(0)
        self.assertEquals(deque.peekFront(), 0)

    def test_pushBack(self):
        deque = Deque()
        # empty
        deque.pushBack("back")
        self.assertEquals(deque.peekFront(), "back")

        # not empty
        deque.pushBack(10)
        self.assertEquals(deque.peekBack(), 10)

    def test_popFront(self):
        # empty
        dequeEmpty = Deque()
        try:
            dequeEmpty.popFront()
            print("test_popFront: FAIL empty")
        except:
            print("test_popFront: PASS empty")
        
        # not empty
        dequeNotEmpty = Deque([0, 1, 2])
        dequeNotEmpty.popFront()
        self.assertEquals(dequeNotEmpty.size(), 2)
        self.assertEquals(dequeNotEmpty.peekFront(), 1)
        self.assertEquals(dequeNotEmpty.peekBack(), 2)

    def test_popBack(self):
        # empty
        dequeEmpty = Deque()
        try:
            dequeEmpty.popBack()
            print("test_popBack: FAIL empty")
        except:
            print("test_popBack: PASS empty")
        
        # not empty
        dequeNotEmpty = Deque([0, 1, 2])
        dequeNotEmpty.popBack()
        self.assertEquals(dequeNotEmpty.size(), 2)
        self.assertEquals(dequeNotEmpty.peekFront(), 0)
        self.assertEquals(dequeNotEmpty.peekBack(), 1)
