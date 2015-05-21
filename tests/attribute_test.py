__author__ = 'John'

import unittest
from attribute import Attribute

class TestAttribute(unittest.TestCase):
    def test_attribute_below_ten_returns_negative_modifier(self):
        attribute = Attribute('Strength', 1)
        self.assertEqual(attribute.get_attribute_modifier(), -5)
        attribute = Attribute('Strength', 2)
        self.assertEqual(attribute.get_attribute_modifier(), -4)
        attribute = Attribute('Strength', 3)
        self.assertEqual(attribute.get_attribute_modifier(), -4)
        attribute = Attribute('Strength', 4)
        self.assertEqual(attribute.get_attribute_modifier(), -3)
        attribute = Attribute('Strength', 8)
        self.assertEqual(attribute.get_attribute_modifier(), -1)
        attribute = Attribute('Strength', 9)
        self.assertEqual(attribute.get_attribute_modifier(), -1)

    def test_attribute_of_ten_returns_zero_modifier(self):
        attribute = Attribute('Strength', 10)
        self.assertEqual(attribute.get_attribute_modifier(), 0)

    def test_attribute_above_ten_returns_positive_modifier(self):
        attribute = Attribute('Strength', 11)
        self.assertEqual(attribute.get_attribute_modifier(), 0)
        attribute = Attribute('Strength', 12)
        self.assertEqual(attribute.get_attribute_modifier(), 1)
        attribute = Attribute('Strength', 13)
        self.assertEqual(attribute.get_attribute_modifier(), 1)
        attribute = Attribute('Strength', 45)
        self.assertEqual(attribute.get_attribute_modifier(), 17)

    def test_attribute_above_forty_five_treated_as_forty_five(self):
        attribute = Attribute('Strength', 56)
        self.assertEqual(attribute.get_attribute_modifier(), 17)
