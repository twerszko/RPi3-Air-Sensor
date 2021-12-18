import unittest

from rolling_registry import RollingRegistry

#from my_sum import sum


class RollingRegistryTest(unittest.TestCase):
    def test_empty_rolling_registry(self):
        registry = RollingRegistry(3)
        
        self.assertEqual(registry.last(), None)
        self.assertEqual(registry.size(), 0)
        self.assertEqual(registry.average(), 0)
        
    def test_non_empty_rolling_registry(self):
        registry = RollingRegistry(4)
        registry.add(1)
        registry.add(2)
        
        self.assertEqual(registry.last(), 2)
        self.assertEqual(registry.size(), 2)
        self.assertEqual(registry.average(), 1.5)
        
    def test_overflowing_rolling_registry(self):
        registry = RollingRegistry(4)
        registry.add(1)
        registry.add(2)
        registry.add(3)
        registry.add(4)
        registry.add(5)
        
        self.assertEqual(registry.last(), 5)
        self.assertEqual(registry.size(), 4)
        self.assertEqual(registry.average(), 3.5)

if __name__ == '__main__':
    unittest.main()
