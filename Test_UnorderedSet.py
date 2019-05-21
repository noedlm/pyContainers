# Create:
# Read: int size (1), bool is_empty (1), bool contains (1)
# Update: void insert (1)
# Delete: void remove (1), void clear (1)

import unittest
from containers.UnorderedSet import UnorderedSet

class TestUnorderedSetListMethods(unittest.TestCase):
    def test_constructor(self):
        # default constructor
        try:
            setDefault = UnorderedSet()
            print("test_constructor: PASS default")
        except:
            print("test_constructor: FAIL default")

        # constructor with data
        try:
            setData = UnorderedSet([3, 1, 2])
            print("test_constructor: PASS constructor with data")
        except:
            print("test_constructor: FAIL constructor with data")

    def test_size(self):
        # empty
        setEmpty = UnorderedSet()
        self.assertEquals(setEmpty.size(), 0)

        # different values
        setDiff = UnorderedSet([2, 1, 3])
        self.assertEquals(setDiff.size(), 3)

        # same value
        setSame = UnorderedSet([2, 2, 2])
        self.assertEquals(setSame.size(), 1)

    def test_is_empty(self):
        # empty
        setEmpty = UnorderedSet()
        self.assertTrue(setEmpty.is_empty())

        # not empty
        setNotEmpty = UnorderedSet([1, 2])
        self.assertFalse(setEmpty.is_empty())

    def test_contains(self):
        # empty
        setEmpty = UnorderedSet()
        self.assertFalse(setEmpty.contains('x'))

        # does not contain
        setDoesNotContain = UnorderedSet(['a', 'z'])
        self.assertFalse(setDoesNotContain.contains('x'))

        # does contain
        setContains = UnorderedSet(['x', 'a', 'z'])
        self.assertTrue(setContains.contains('x'))

    def test_add(self):
        setAdd = UnorderedSet()

        # empty
        setAdd.add('b')
        self.assertEquals(setAdd.size(), 1)
        self.assertTrue(setAdd.contains('b'))

        # same value
        setAdd.add('b')
        self.assertEquals(setAdd.size(), 1)

        # different value
        setAdd.add('a')
        self.assertEquals(setAdd.size(), 2)
        self.assertTrue(setAdd.contains('a'))

        # different type
        self.assertRaises(TypeError, setAdd(3))

    def test_remove(self):
        setRem = UnorderedSet()

        # empty
        setRem.remove(5)
        self.assertEquals(setRem.size(), 0)

        setRem.insert(1)
        setRem.insert(9)
        setRem.insert(0)

        # value exists
        setRem.remove(9)
        self.assertEquals(setRem.size(), 2)

        # value doesn't exist
        setRem.remove(9)
        self.assertEquals(setRem.size(), 2)

    def test_clear(self):
        setClr = UnorderedSet([1])
        setClr.clear();
        self.assertEquals(setClr.size(), 0)
