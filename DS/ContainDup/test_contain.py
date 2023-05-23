import unittest
from DS.ContainDup.contain import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_contains_duplicate_true(self):
        self.assertTrue(self.sol.containsDuplicate([1,2,3,1]))
        self.assertTrue(self.sol.containsDuplicate([1,1,1,1]))
        self.assertTrue(self.sol.containsDuplicate([1,2,3,2]))
        self.assertTrue(self.sol.containsDuplicate([1]*10000 + [2]))

    def test_contains_duplicate_false(self):
        self.assertFalse(self.sol.containsDuplicate([1,2,3]))
        self.assertFalse(self.sol.containsDuplicate([]))
        self.assertFalse(self.sol.containsDuplicate([1]))
        self.assertFalse(self.sol.containsDuplicate(list(range(10000))))

if __name__ == '__main__':
    unittest.main()
