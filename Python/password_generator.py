import string
import secrets

class PasswordGenerator:
  def __init__(self, length, use_upper=True, use_digits=True, use_lower=True, use_symbols=True):
    self.length = length
    self.use_upper = use_upper
    self.use_digits = use_digits
    self.use_lower = use_lower
    self.use_symbols = use_symbols

  def generate(self):
    characters =""

    if self.use_upper:
      characters +=string.ascii_uppercase
    if self.use_lower:
      characters +=string.ascii_lowercase
    if self.use_digits:
      characters +=string.digits
    if self.use_symbols:
      characters +=string.punctuation

    if not characters:
      raise ValueError("At least one character set must be selected")
    
    password = ''.join(secrets.choice(characters) for _ in range(self.length))
    return password
  
  def generate_multiple(self, count):
    return [self.generate() for _ in range(count)]
  
if __name__ == "__main__":
  print("Password Generator")
  length = int(input("Enter password length: "))
  upper = input( "Include uppercase letters? (y/n): ").lower() == 'y'
  lower = input("Include lowercase letters? (y/n): ").lower() =='y'
  digits= input("Include digits? (y/n): ").lower() == 'y'
  symbols = input("Include symbols? (y/n): ").lower() == 'y'

  gen = PasswordGenerator(length, use_upper=upper, use_lower=lower, use_digits=digits, use_symbols=symbols)
  print("Generated Password: ", gen.generate())