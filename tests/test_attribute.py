__author__ = 'John Mullins'

import unittest
from attribute import Attribute


class TestAttribute(unittest.TestCase):

    def test_attribute_score_returns_correct_modifier(self):
        for attribute_values in self.get_negative_test_attribute_values():
            for attribute_name in Attribute.ABILITY_SCORE_NAMES:
                attribute = Attribute(attribute_name, attribute_values[0])
                self.assertEqual(attribute.get_attribute_modifier().value, attribute_values[1])

    def test_attribute_above_forty_five_set_to_forty_five(self):
        attribute = Attribute(Attribute.DEXTERITY, 56)
        self.assertEqual(attribute.get_attribute_modifier().value, 17)

    def test_attribute_below_one_set_to_one(self):
        attribute = Attribute(Attribute.WISDOM, -15)
        self.assertEqual(attribute.get_attribute_modifier().value, -5)

    def test_attribute_rejects_bad_attribute_name(self):
        with self.assertRaisesRegexp(ValueError, 'not_a_valid_name is not a recognized ability score'):
            Attribute('not_a_valid_name', 13)

    def test_attribute_name_constant_resolves_to_correct_name(self):
        for name_pair in self.get_attribute_name_pairs():
            self.assertEqual(name_pair[0], name_pair[1])

    def test_attribute_get_modifier_returns_modifier_object(self):
        attribute = Attribute(Attribute.DEXTERITY, 32)
        self.assertEqual(
            attribute.get_attribute_modifier().audit_explanation,
            '+11, Dexterity ability score of 32. '
        )

    def get_negative_test_attribute_values(self):
        # inner lists in [attribute, modifier] format
        return [
            [1, -5],
            [2, -4], [3, -4],
            [4, -3], [5, -3],
            [6, -2], [7, -2],
            [8, -1], [9, -1],
            [10, 0], [11, 0],
            [12, 1], [13, 1],
            [14, 2], [15, 2],
            [16, 3], [17, 3],
            [18, 4], [19, 4],
            [20, 5], [21, 5],
            [22, 6], [23, 6],
            [24, 7], [25, 7],
            [26, 8], [27, 8],
            [28, 9], [29, 9],
            [30, 10], [31, 10],
            [32, 11], [33, 11],
            [34, 12], [35, 12],
            [36, 13], [37, 13],
            [38, 14], [39, 14],
            [40, 15], [41, 15],
            [42, 16], [43, 16],
            [44, 17], [45, 17]
        ]

    def get_attribute_name_pairs(self):
        # inner list in [class_constant, expected name] format
        return [
            [Attribute.STRENGTH, 'Strength'],
            [Attribute.CONSTITUTION, 'Constitution'],
            [Attribute.WISDOM, 'Wisdom'],
            [Attribute.DEXTERITY, 'Dexterity']
        ]
