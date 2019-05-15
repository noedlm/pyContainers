'''
Create:
Read: int size (1), <T> get (log n), [<T>] keys (n), bool contains (log n), bool is_empty (1)
Update: void put (log n) 
Delete: void clear (1), <T> remove (log n)
'''
import unittest
from containers.OrderedMap import OrderedMap

class TestOrderedMapMethods(unittest.TestCase):
    def test_initiate_ordered_map(self):
        try:
            orderedMap = OrderedMap()
            print("test_constructor: PASS")
        except:
            print("test_constructor: FAIL")

    def test_size_empty_map(self):
        orderedMap = OrderedMap()
        self.assertEqual(orderedMap.size(), 0)

    def test_is_empty(self):
        orderedMap = OrderedMap()
        self.assertTrue(orderedMap.is_empty())

    def test_put(self):
        orderedMap = OrderedMap()
        orderedMap.put('key', 'value')
        self.assertEqual(orderedMap.size(), 1)

    def test_put_duplicate_key(self):
        orderedMap = OrderedMap()
        orderedMap.put('key', 'value')
        orderedMap.put('key', 'newValue')
        self.assertEqual(orderedMap.size(), 1)

    def test_put_key_type_error(self):
        orderedMap = OrderedMap()
        orderedMap.put('key', 'value')
        self.assertRaises(TypeError, orderedMap.put(2, 'a'))

    def test_put_value_type_error(self):
        orderedMap = OrderedMap()
        orderedMap.put('key', 'value')
        self.assertRaises(TypeError, orderedMap.put('k', 4))


    def test_get(self):
        orderedMap = OrderedMap()
        orderedMap.put('key', 'value')
        self.assertEqual(orderedMap.get('key'), 'value')

    def test_remove_key(self);
        orderedMap = OrderedMap()
        orderedMap.put('key', 'value')
        orderedMap.remove('key')
        self.assertFalse(orderedMap.size())


    def test_contains_key(self):
        orderedMap = OrderedMap()
        orderedMap.put('key', 'value')
        self.assertTrue(orderedMap.contains('key'))

    def test_clear(self):
        orderedMap = OrderedMap()
        orderedMap.put('key', 'value')
        orderedMap.clear()
        self.assertEqual(orderedMap.size(), 0)

    def test_key_set(self):
        orderedMap = OrderedMap()
        orderedMap.put('c', 1)
        orderedMap.put('a', 2)
        orderedMap.put('b', 3)
        self.assertEqual(orderedMap.keys(), ['a', 'b', 'c'])

