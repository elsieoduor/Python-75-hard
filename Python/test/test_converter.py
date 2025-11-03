import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from unit_converter import UnitConverter

class TestUnitConverter(unittest.TestCase):
  def setUp(self):
    self.converter = UnitConverter()

  def test_length(self):
    c = self.converter.convert
    self.assertAlmostEqual(c(1, "km", "m", "length"), 1000)
    self.assertAlmostEqual(c(1, "km", "m", "length"), 1000)
    self.assertAlmostEqual(c(100, "cm", "m", "length"), 1)
    self.assertAlmostEqual(c(1000, "mm", "m", "length"), 1)
    self.assertAlmostEqual(round(c(1, "mi", "km", "length"), 3), 1.609)
    self.assertAlmostEqual(round(c(1, "yd", "ft", "length"), 3), 3.000)
    self.assertAlmostEqual(round(c(1, "ft", "in", "length"), 3), 12.000)
    self.assertAlmostEqual(round(c(1, "m", "ft", "length"), 4), 3.2808)
    self.assertAlmostEqual(round(c(1, "in", "cm", "length"), 2), 2.54)
  
  def test_weight(self):
    c = self.converter.convert
    self.assertAlmostEqual(c(1, "kg", "g", "weight"), 1000)
    self.assertAlmostEqual(c(1000, "g", "kg", "weight"), 1)
    self.assertAlmostEqual(round(c(1, "lb", "kg", "weight"), 6), 0.453592)
    self.assertAlmostEqual(round(c(16, "oz", "lb", "weight"), 3), 1.000)
    self.assertAlmostEqual(round(c(1, "ton", "kg", "weight"), 3), 1000.000)
    self.assertAlmostEqual(round(c(1, "kg", "lb", "weight"), 3), 2.205)

  def test_volume(self):
    c = self.converter.convert
    self.assertAlmostEqual(c(1, "l", "ml", "volume"), 1000)
    self.assertAlmostEqual(round(c(1, "gal", "l", "volume"), 5), 3.78541)
    self.assertAlmostEqual(round(c(1, "qt", "l", "volume"), 6), 0.946353)
    self.assertAlmostEqual(round(c(1, "pt", "l", "volume"), 6), 0.473176)
    self.assertAlmostEqual(round(c(1, "cup", "ml", "volume"), 1), 240)
    self.assertAlmostEqual(round(c(1000, "ml", "gal", "volume"), 3), 0.264)
  
  def test_time(self):
    c = self.converter.convert
    self.assertAlmostEqual(c(60, "s", "min", "time"), 1)
    self.assertAlmostEqual(c(3600, "s", "hr", "time"), 1)
    self.assertAlmostEqual(c(24, "hr", "day", "time"), 1)
    self.assertAlmostEqual(c(7, "day", "week", "time"), 1)
    self.assertAlmostEqual(c(1, "week", "s", "time"), 604800)
  
  def test_speed(self):
    c = self.converter.convert
    self.assertAlmostEqual(c(1, "m/s", "km/h", "speed"), 3.6, places=3)
    self.assertAlmostEqual(round(c(1, "km/h", "m/s", "speed"), 6), 0.277778)
    self.assertAlmostEqual(round(c(60, "mph", "km/h", "speed"), 1), 96.6)
    self.assertAlmostEqual(round(c(10, "ft/s", "m/s", "speed"), 4), 3.048)
    self.assertAlmostEqual(round(c(100, "km/h", "mph", "speed"), 1), 62.1)

  def test_temperature(self):
    t = self.converter.convert_temperature
    self.assertAlmostEqual(round(t(0, "c", "f"), 2), 32.00)
    self.assertAlmostEqual(round(t(32, "f", "c"), 2), 0.00)
    self.assertAlmostEqual(round(t(0, "c", "k"), 2), 273.15)
    self.assertAlmostEqual(round(t(273.15, "k", "c"), 2), 0.00)
    self.assertAlmostEqual(round(t(100, "c", "f"), 2), 212.00)
    self.assertAlmostEqual(round(t(-40, "c", "f"), 2), -40.00)
    self.assertAlmostEqual(round(t(212, "f", "k"), 2), 373.15)

if __name__ == "__main__":
    unittest.main()