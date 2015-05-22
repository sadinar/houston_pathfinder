__author__ = 'John Mullins'

import unittest
from attribute import Attribute

class TestAttribute(unittest.TestCase):
    def test_attribute_below_ten_returns_negative_modifier(self):
        attribute = Attribute(Attribute.STRENGTH, 1)
        self.assertEqual(attribute.get_attribute_modifier(), -5)
        attribute = Attribute(Attribute.STRENGTH, 6)
        self.assertEqual(attribute.get_attribute_modifier(), -2)
        attribute = Attribute(Attribute.STRENGTH, 7)
        self.assertEqual(attribute.get_attribute_modifier(), -2)
        attribute = Attribute(Attribute.STRENGTH, 9)
        self.assertEqual(attribute.get_attribute_modifier(), -1)

    def test_attribute_above_nine_below_twelve_returns_zero_modifier(self):
        attribute = Attribute(Attribute.STRENGTH, 10)
        self.assertEqual(attribute.get_attribute_modifier(), 0)
        attribute = Attribute(Attribute.STRENGTH, 11)
        self.assertEqual(attribute.get_attribute_modifier(), 0)

    def test_attribute_above_eleven_returns_positive_modifier(self):
        attribute = Attribute(Attribute.STRENGTH, 12)
        self.assertEqual(attribute.get_attribute_modifier(), 1)
        attribute = Attribute(Attribute.STRENGTH, 13)
        self.assertEqual(attribute.get_attribute_modifier(), 1)
        attribute = Attribute(Attribute.STRENGTH, 14)
        self.assertEqual(attribute.get_attribute_modifier(), 2)
        attribute = Attribute(Attribute.STRENGTH, 45)
        self.assertEqual(attribute.get_attribute_modifier(), 17)

    def test_attribute_above_forty_five_treated_as_forty_five(self):
        attribute = Attribute(Attribute.STRENGTH, 56)
        self.assertEqual(attribute.get_attribute_modifier(), 17)

    def test_attribute_rejects_bad_attribute_name(self):
        with self.assertRaisesRegexp(ValueError, 'not_a_valid_name is not a recognized ability score'):
            Attribute('not_a_valid_name', 13)

    def test_strength_constant_resolves_to_strength(self):
        self.assertEqual(Attribute.STRENGTH, 'Strength')

    def test_constitution_constant_resolves_to_constitution(self):
        self.assertEqual(Attribute.CONSTITUTION, 'Constitution')
