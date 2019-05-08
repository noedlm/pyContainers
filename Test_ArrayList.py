# Create:
# Read: size, isEmpty, at
# Update: insert, append, []?, replace?, get?, at?
# Delete: remove

import unittest
from containers.ArrayList import ArrayList

class TestArrayListMethods(unittest.TestCase):
    def test_constructor(self):
        # default constructor
        try:
            arrayListDefault = ArrayList()
            print("test_constructor: PASS default")
        except:
            print("test_constructor: FAIL default")

        # constructor with data
        try:
            arrayListData = ArrayList([0, 1, 2])
            print("test_constructor: PASS constructor with data")
        except:
            print("test_constructor: FAIL constructor with data")

    def test_size(self):
        # default size
        arrayListEmpty = ArrayList()
        self.assertEquals(arrayListEmpty.size(), 0)

        # same element type
        arrayListContents = ArrayList([0, 1, 2])
        self.assertEquals(arrayListContents.size(), 3)

        # different element types
        arrayListSame = ArrayList([0, "string", 1.1])
        self.assertEquals(arrayListSame.size(), 3)

    def test_isEmpty(self):
        # is empty
        arrayListEmpty = ArrayList()
        self.assertTrue(arrayListEmpty.isEmpty())

        # is not empty
        arrayListNotEmpty = ArrayList([0])
        self.assertFalse(arrayListNotEmpty.isEmpty())

    def test_append(self):
        testArrayList = ArrayList()

        # append
        testArrayList.append(0)
        self.assertEquals(testArrayList.size(), 1)

        # append different type
        testArrayList.append('x')
        self.assertEquals(testArrayList.size(), 2)

    def test_at(self):
        testArrayList = ArrayList("first")

        # at first position
        self.assertEquals(testArrayList.at(0), "first")

        # at negative position
        try:
            atNegativePos = testArrayList.at(-2)
            print("test_at: FAIL .at() negative position")
        except:
            print("test_at: PASS .at() negative position")

        try:
            atLargerSize = testArrayList.at(5)
            print("test_at: FAIL .at() position greater than max")
        except:
            print("test_at: PASS .at() position greater than max")

    def test_insert(self):
        testArrayList = ArrayList()

        # insert out of bounds on empty
        try:
            testArrayList.insert(5, "can't do this")
            print("test_insert: FAIL out of bounds on empty")
        except:
            print("test_insert: PASS out of bounds on empty")

        # insert on empty
        testArrayList.insert(0, "first")
        self.assertEquals(testArrayList.at(0), "first")

        # insert out of bounds
        try:
            testArrayList.insert(5, "can't do this")
            print("test_insert: FAIL out of bounds")
        except:
            print("test_insert: PASS out of bounds")

        # insert after
        testArrayList.insert(1, "second")
        self.assertEquals(testArrayList.at(1), "second")

        # insert before
        testArrayList.insert(0, "third")
        self.assertEquals(testArrayList.at(0), "third")
        self.assertEquals(testArrayList.at(1), "first")
        self.assertEquals(testArrayList.at(2), "second")

    def test_replace(self):
        testArrayList = ArrayList()

        # replace empty
        try:
            testArrayList.replace(0, 10)
            print("test_replace: FAIL empty")
        except:
            print("test_replace: PASS empty")

        testArrayList.append(0)
        testArrayList.append(1)
        testArrayList.append(2)

        # replace out of bounds
        try:
            testArrayList.replace(5, 10)
            print("test_replace: FAIL out of bounds")
        except:
            print("test_replace: PASS out of bounds")

        # replace value
        testArrayList.replace(1, 10)
        self.assertEquals(testArrayList.at(1), 10)

        # replace type
        testArrayList.replace(0, "zero")
        self.assertEquals(testArrayList.at(0), "zero")

    def test_remove(self):
        testArrayList = ArrayList()

        # remove empty
        try:
            testArrayList.remove(1)
            print("test_remove: FAIL empty")
        except:
            print("test_remove: PASS empty")

        testArrayList.append(0)
        testArrayList.append(1)
        testArrayList.append(2)

        # remove out of bounds
        try:
            testArrayList.remove(5)
            print("test_remove: FAIL out of bounds")
        except:
            print("test_remove: PASS out of bounds")

        # remove at position
        testArrayList.remove(1)
        self.assertEquals(testArrayList.size(), 2)
        self.assertEquals(testArrayList.at(1), 2)
