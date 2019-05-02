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
		try:
			u_map = UnorderedMap()
			u_map.size()
			print('TEST SIZE: PASS')
		except:
			print('TEST SIZE: FAIL')

	def test_put(self):
		try:
			u_map = UnorderedMap()
			u_map.put('a',1)
			print('TEST.put: PASS')
		except:
			print('TEST.put: FAIL')
		u_map = UnorderedMap()
		u_map.put('a',1)
		u_map.put('b',2)
		self.assertEqual(UnorderedMap.size(), 2)

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
		self.assertEqual(u_map.key_set(), ['a','b'])

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

    def test_iterator(self):
        u_map = UnorderedMap()
        u_map.put('a',2)
		u_map.put('b',3)
		u_map.put('c',1)
        self.assertEqual(sorted(u_map.key_set()), [1,2,3])