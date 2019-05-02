import unittest
from containers.orderedset import OrderedSet

class TestOrderedSetMethods(unittest.TestMethod):
	def test_constructor(self):
		try:
			orderedset_a = OrderedSet()
			orderedset_b = OrderedSet([1,2,3,4,5])
			print('TEST CONSTRUCTOR: PASS')
		except:
			print('TEST CONSTRUCTOR: FAIL')

	def test_size(self):
		try:
			orderedset = OrderedSet()
			orderedset.size()
			print('TEST SIZE: PASS')
		except:
			print('TEST SIZE: FAIL')

	def test_list_initialization(self):
		orderedset_a = OrderedSet([1,2,3,4,5])
		self.assertEqual(orderedset_a.size(), 5)
		orderedset_b = OrderedSet([1,1,1,1,1])
		self.assertEqual(orderedset_b.size(), 1)

	def test_add(self):
		try:
			orderedset = OrderedSet()
			orderedset.add(5)
			print('TEST ADD: PASS')
		except:
			print('TEST ADD: FAIL')
		orderedset = OrderedSet()
		orderedset.add(1)
		orderedset.add(2)
		self.assertEqual(orderedset.size(), 2)
		orderedset.add(2)
		self.assertEqual(orderedset.size(), 2)

    def test_contains(self):
        orderedset = OrderedSet([3,5,1,2,4])
        self.assertTrue(orderedset.contains(2))
        self.assertFalse(orderedset.contains(6))

    def test_remove(self):
        orderedset = OrderedSet([3,5,1,2,4])
        orderedset.remove(2)
        self.assertEqual(orderedset.size(), 4)
        self.assertFalse(orderedset.contains(4))

	def test_clear(self):
        orderedset = OrderedSet([1,2,3,4,5])
        orderedset.clear()
        self.assertEqual(orderedset, OrderedSet())

    def test_first_last(self):
        orderedset = OrderedSet([3,5,1,2,4])
        self.assertEqual(orderedset.first(), 1)
        self.assertEqual(orderedset.last(), 5)

    def test_iterator(self):
        orderedset = OrderedSet([3,5,1,2,4])
        arr = []
        for x in orderedset:
            arr.append(x)
        self.assertEqual(arr, [1,2,3,4,5])
