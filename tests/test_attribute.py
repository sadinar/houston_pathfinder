__author__ = 'John Mullins'

import unittest
from attribute import Attribute

class TestAttribute(unittest.TestCase):
    def test_attribute_below_ten_returns_negative_modifier(self):
        attribute = Attribute('Strength', 1)
        self.assertEqual(attribute.get_attribute_modifier(), -5)
        attribute = Attribute('Strength', 6)
        self.assertEqual(attribute.get_attribute_modifier(), -2)
        attribute = Attribute('Strength', 7)
        self.assertEqual(attribute.get_attribute_modifier(), -2)
        attribute = Attribute('Strength', 9)
        self.assertEqual(attribute.get_attribute_modifier(), -1)

    def test_attribute_above_nine_below_twelve_returns_zero_modifier(self):
        attribute = Attribute('Strength', 10)
        self.assertEqual(attribute.get_attribute_modifier(), 0)
        attribute = Attribute('Strength', 11)
        self.assertEqual(attribute.get_attribute_modifier(), 0)

    def test_attribute_above_eleven_returns_positive_modifier(self):
        attribute = Attribute('Strength', 12)
        self.assertEqual(attribute.get_attribute_modifier(), 1)
        attribute = Attribute('Strength', 13)
        self.assertEqual(attribute.get_attribute_modifier(), 1)
        attribute = Attribute('Strength', 14)
        self.assertEqual(attribute.get_attribute_modifier(), 2)
        attribute = Attribute('Strength', 45)
        self.assertEqual(attribute.get_attribute_modifier(), 17)

    def test_attribute_above_forty_five_treated_as_forty_five(self):
        attribute = Attribute('Strength', 56)
        self.assertEqual(attribute.get_attribute_modifier(), 17)
