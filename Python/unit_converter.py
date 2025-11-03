import json

class UnitConverter:
  def __init__(self):
    self.length_units = {
      "m": 1.0,
      "cm": 0.01,
      "mm": 0.001,
      "km": 1000.0,
      "in": 0.0254,
      "ft": 0.3048,
      "yd": 0.9144,
      "mi": 1609.34,
    }
    self.weight_units ={
      "kg": 1.0,
      "g": 0.001,
      "mg": 0.000001,
      "lb": 0.453592,
      "oz": 0.0283495,
      "ton": 1000.0,
    }
    self.volume_units ={
      "l": 1.0,
      "ml": 0.001,
      "gal": 3.78541,
      "qt": 0.946353,
      "pt": 0.473176,
      "cup": 0.24,
    }
    self.time_units={
      "s": 1.0,
      "min": 60.0,
      "hr": 3600.0,
      "day": 86400.0,
      "week": 604800.0,
    }
    self.speed_units={
      "m/s": 1.0,
      "km/h": 0.277778,
      "mph": 0.44704,
      "ft/s": 0.3048,
    }
  
  def convert(self, value, from_unit, to_unit, category):
    categories ={
      'length': self.length_units,
      'weight': self.weight_units,
      'volume': self.volume_units,
      'time': self.time_units,
      'speed': self.speed_units
    }

    if category not in categories:
      raise ValueError('Invalid category')
    
    units = categories[category]

    if from_unit not in units or to_unit not in units:
      raise ValueError('Invalid unit for the selected category')
    
    base_value = value * units[from_unit]
    converted = base_value/ units[to_unit]
    return converted
  
  def convert_temperature(self, value, from_unit, to_unit):
    from_unit, to_unit = from_unit.lower(), to_unit.lower()

    if from_unit == to_unit:
      return value
    
    #To Celsius
    if from_unit == 'c':
      c = value
    elif from_unit =='f':
      c = (value -32) *5/9
    elif from_unit == 'k':
      c = value -273.15
    else:
      raise ValueError('Invalid temperature unit')
    
    #From Celsius
    if to_unit == 'c':
      return c
    elif to_unit == 'f':
      return (c * 9/5) + 32
    elif to_unit == 'k':
      return c + 273.15
    else:
      raise ValueError('Invalid temperature unit')

    
#CLI Interface
if __name__ == "__main__":
  converter = UnitConverter()

  print("Welcome to the Unit Converter")
  print("Select category: Length, Weight, Volume, Time, Speed, Temperature")
  category = input("Category: ").strip().lower()

  if category == 'temperature':
    value= float(input("Enter a value to convert: "))
    from_unit = input("From unit (C,F,K): ").strip().lower()
    to_unit = input("To unit(C,F,K): ").strip().lower()
    result = converter.convert_temperature(value, from_unit, to_unit)
  
  else:
    value = float(input("Enter a value to convert: "))
    from_unit = input("From unit: ").strip().lower()
    to_unit = input("To unit: ").strip().lower()
    result = converter.convert(value, from_unit, to_unit, category)
    
  print(f"{value} {from_unit.upper()} = {result} {to_unit.upper()}")


