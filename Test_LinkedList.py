'''
Create:
Read: int size (1), bool is_empty (1), <T> at (n)
Update: void append (1), void insert (n), void replace (n)
Delete: void clear (1), <T> remove (n)
'''
import unittest
from containers.linkedList import LinkedList

class TestLinkedListMethods(unittest.TestCase):
    def test_empty_constructor(self):
        try:
            linkedList = LinkedList()
            print("test_constructor: PASS")
        except:
            print("test_constructor: FAIL")

    def test_constructor_with_data(self):
        try:
            linkedList = LinkedList([1,2,3,4,5])
            print("test_constructor_with_data: PASS")
        except:
            print("test_constructor_with_data: FAIL")

    def test_constructor_multiple_data_types(self):
        self.assertRaises(TypeError, LinkedList([1,'a', None]))


    def test_size_empty(self):
        emptyList = LinkedList()
        self.assertEqual(emptyList.size(), 0)

    def test_size(self):
        linkedList = LinkedList([1,2,3,4])
        self.assertEqual(linkedList.size(), 4)

    def test_get_value_at_index(self):
        linkedList = LinkedList([1,2,3,4])
        try:
            linkedlist.at(1)
            print("test_get_value_at_index: PASS")
        except:
            print("test_get_value_at_index: FAIL")

        self.assertEqual(linkedList.at(1), 2)

    def test_is_empty(self):
        emptyList = LinkedList()
        self.assertTrue(emptyList.is_empty())

    def test_is_empty_with_populated_list(self):
        linkedList = LinkedList([1,2,3,4])
        self.assertFalse(linkedList.is_empty())

    def test_append(self):
        emptyList = LinkedList()
        emptyList.append(2)
        self.assertEqual(emptyList.at(0), 2)

    def test_insert(self):
        linkedList = LinkedList([2,3,4])
        linkedList.insert(0, 1)
        self.assertEqual(linkedList.at(0), 1)
        self.assertEqual(linkedList.size(), 4)

    def test_replace(self):
        linkedList = LinkedList([1,2,3,4])
        linkedList.replace(1, 5)
        self.assertEqual(linkedList.at(1), 5)
        self.assertEqual(linkedList.size(), 4)

    def test_remove(self):
        linkedList = LinkedList([1,2,3,4])
        linkedList.remove(1)
        self.assertEqual(linkedList.size(), 3)
        self.assertEqual(linkedList.at(1), 3)

    def test_clear(self)
        linkedList = LinkedList([1,2,3,4])
        linkedList.clear()
        self.assertTrue(linkedList.is_empty())