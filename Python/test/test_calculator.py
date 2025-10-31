import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from calculator import add, subtract, multiply, divide, power, modulus, floor_divide, square_root

class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(23, 9), 32)
    self.assertEqual(add(6, 10), 16)

  def test_subtract(self):
    self.assertEqual(subtract(23, 9), 14)
    self.assertEqual(subtract(10, 6), 4)

  def test_multiply(self):
    self.assertEqual(multiply(23, 9), 207)
    self.assertEqual(multiply(6, 10), 60)
  
  def test_divide(self):
    self.assertEqual(divide(23, 9), 23/9)
    self.assertEqual(divide(10, 2), 5)
    with self.assertRaises(ValueError):
      divide(10, 0)
  
  def test_power(self):
    self.assertEqual(power(2, 3), 8)
    self.assertEqual(power(5, 0), 1)

  def test_modulus(self):
    self.assertEqual(modulus(23, 9), 5)
    self.assertEqual(modulus(10, 3), 1)

  def test_floor_divide(self):
    self.assertEqual(floor_divide(23, 9), 2)
    self.assertEqual(floor_divide(10, 3), 3)
    with self.assertRaises(ValueError):
      floor_divide(10, 0)
  
  def test_square_root(self):
    self.assertEqual(square_root(16), 4)
    self.assertEqual(square_root(25), 5)
    with self.assertRaises(ValueError):
      square_root(-4)

if __name__ == '__main__':
    unittest.main()
