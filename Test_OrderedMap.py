import unittest
from containers.OrderedMap import OrderedMap

class TestOrderedMapMethods(unittest.TestCase):
    def test_initiate_ordered_map(self):
        orderedMap = OrderedMap()
        self.assertEqual(orderedMap, {})
    
    def test_initiate_ordered_map_with_values(self):
        orderedMap = OrderedMap({'key': 'value'})
        self.assertEqual(orderedMap, {'key': 'value'})

    def test_add(self):
        orderedMap = OrderedMap()
        orderedMap.add('key', 'value')
        self.assertEqual(orderedMap, {'key': 'value'})

    def test_remove_key(self);
        orderedMap = OrderedMap({'key': 'value'})
        orderedMap.remove('key')
        self.assertEqual(orderedMap, {})

    def test_size(self):
        orderedMap = OrderedMap({'key': 'value'})
        self.assertEqual(orderedMap.size(), 1)

    def test_get(self):
        orderedMap = OrderedMap({'key': 'value'})
        self.assertEqual(orderedMap.get('key'), 'value')

    def test_contains_key(self):
        orderedMap = OrderedMap({'key': 'value'})
        self.assertEqual(orderedMap.contains('keyu'), True)

    def test_clear(self):
        orderedMap = OrderedMap({'key': 'value'})
        self.assertEqual(orderedMap.clear(), {})

    def test_keys_order(self):
        orderedMap = OrderedMap({'c': 1, 'a': 2, 'b': 3})
        self.assertEqual(orderedMap, {'a': 2, 'b': 3, 'c': 1})

    def test_key_set(self):
        orderedMap = OrderedMap({'c': 1, 'a': 2, 'b': 3})
        self.assertEqual(orderedMap.keys(), ['a', 'b', 'c'])
