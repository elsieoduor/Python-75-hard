import unittest
import os
import sys
import string

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from password_generator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = PasswordGenerator(length=12)

    def test_password_length(self):
        pw = self.gen.generate()
        self.assertEqual(len(pw), 12)

    def test_includes_uppercase(self):
        gen = PasswordGenerator(length=20, use_lower=False, use_digits=False, use_symbols=False)
        pw = gen.generate()
        self.assertTrue(all(c in string.ascii_uppercase for c in pw))

    def test_includes_digits(self):
        gen = PasswordGenerator(length=10, use_upper=False, use_lower=False, use_digits=True, use_symbols=False)
        pw = gen.generate()
        self.assertTrue(all(c in string.digits for c in pw))

    def test_symbols_and_letters(self):
        gen = PasswordGenerator(length=15, use_symbols=True)
        pw = gen.generate()
        self.assertTrue(any(c in string.punctuation for c in pw))

    def test_multiple_passwords(self):
        passwords = self.gen.generate_multiple(5)
        self.assertEqual(len(passwords), 5)
        self.assertEqual(len(passwords[0]), 12)
        self.assertNotEqual(passwords[0], passwords[1])

    def test_no_character_sets_selected(self):
        gen = PasswordGenerator(length=10, use_upper=False, use_lower=False, use_digits=False, use_symbols=False)
        with self.assertRaises(ValueError):
            gen.generate()


if __name__ == "__main__":
    unittest.main()
