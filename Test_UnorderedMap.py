# Create:
# Read: int size (1), <T> get (1), bool contains_key (1), [<T>] key_set (n)
# Update: void put (1)
# Delete: <T> remove (1), void clear (1)

import unittest
from containers.UnorderedMap import UnorderedMap

class TestUnorderedMapMethods(unittest.TestMethod):
    def test_constructor(self):
        try:
            u_map = UnorderedMap()
            print('TEST CONSTRUCTOR: PASS')
        except:
            print('TEST CONSTRUCTOR: FAIL')

    def test_size(self):
        u_map = UnorderedMap()
        self.assetEqual(u_map.size(), 0)

    def test_put(self):
        u_map = UnorderedMap()
        u_map.put('a',1)
        u_map.put('b',2)
        self.assertEqual(UnorderedMap.size(), 2)

    def test_type_error_key(self):
        u_map = UnorderedMap()
        u_map.put('a',1)
        u_map.assertRaises(TypeError, u_map.put(1, 1))

    def test_type_error_value(self):
        u_map = UnorderedMap()
        u_map.put('a',1)
        u_map.assertRaises(TypeError, u_map.put('b', 'b'))

    def test_get(sef):
        u_map = UnorderedMap()
        u_map.put('a',1)
        u_map.put('b',2)
        self.assertEqual(u_map.get('a'), 1)
        self.assertEqual(u_map.get('c'), None)

    def test_contains_key(self):
        u_map = UnorderedMap()
        u_map.put('a',1)
        u_map.put('b',2)
        self.assertTrue(u_map.contains_key('a'))
        self.assertFalse(u_map.contains_key('c'))

    def test_keyset(self):
        u_map = UnorderedMap()
        u_map.put('a',1)
        u_map.put('b',2)
        self.assertEqual(sorted(u_map.key_set()), ['a','b'])

    def test_remove(self):
        u_map = UnorderedMap()
        u_map.put('a',1)
        u_map.put('b',2)
        u_map.put('c',3)
        u_map.put('d',4)
        u_map.remove('b')
        self.assertEqual(u_map.size(), 3)
        u_map.remove('e')
        self.assertEqual(u_map.size(), 3)

    def test_clear(self):
        u_map = UnorderedMap()
        u_map.put('a',1)
        u_map.put('b',2)
        u_map.put('c',3)
        u_map.clear()
        self.assertEqual(u_map, UnorderedMap())