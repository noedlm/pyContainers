# Create:
# Read: int size (1), bool is_empty (1), <T> at (1)
# Update: void insert (n), void append (1), void replace (1)
# Delete: <T> remove (n), void clear (1)

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

    def test_is_empty(self):
        # is empty
        arrayListEmpty = ArrayList()
        self.assertTrue(arrayListEmpty.is_empty())

        # is not empty
        arrayListNotEmpty = ArrayList([0])
        self.assertFalse(arrayListNotEmpty.is_empty())

    def test_append(self):
        testArrayList = ArrayList()

        # append
        testArrayList.append(0)
        self.assertEquals(testArrayList.size(), 1)

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

        # at position greater than max
        try:
            atLargerSize = testArrayList.at(5)
            print("test_at: FAIL .at() position greater than max")
        except:
            print("test_at: PASS .at() position greater than max")

    def test_insert(self):
        testArrayList = ArrayList()

        # insert out of bounds
        try:
            testArrayList.insert(5, "can't do this")
            print("test_insert: FAIL out of bounds")
        except:
            print("test_insert: PASS out of bounds")

        # insert on empty
        testArrayList.insert(0, "first")
        self.assertEquals(testArrayList.at(0), "first")

        # insert after
        testArrayList.insert(1, "second")
        self.assertEquals(testArrayList.at(1), "second")

        # insert before
        testArrayList.insert(0, "third")
        self.assertEquals(testArrayList.at(0), "third")
        self.assertEquals(testArrayList.at(1), "first")
        self.assertEquals(testArrayList.at(2), "second")

        # insert different type
        self.assertRaises(TypeError, testArrayList.insert(1, 10))

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

        # replace value
        testArrayList.replace(1, 10)
        self.assertEquals(testArrayList.at(1), 10)

        # replace different type
        self.assertRaises(TypeError, testArrayList.replace(1, "ten"))

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
