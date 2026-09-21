import unittest
from src.calculator import add, subtract, divide 

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(-2, -4), 2)
        self.assertEqual(subtract(3, -3), 6)
        self.assertEqual(subtract(-2, 4), -6)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(2, -1), -2)
        self.assertEqual(divide(4, 0), 0)

if __name__ == '__main__':
   unittest.main() 