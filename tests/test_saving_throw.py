__author__ = 'John Mullins'

import unittest
from saving_throws.will import Will
from actor import Actor
from attribute import Attribute
from character_classes.fighter import Fighter


class TestSavingThrow(unittest.TestCase):

    def test_add_attribute_to_save_bonus_ignores_duplicates(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 5)], [Fighter(3)])
        will_save = Will(actor)
        self.assertEqual(will_save.modifier.value, -2)
        self.assertEqual(will_save.applicable_attributes[0], Attribute.WISDOM)

        will_save.add_attribute_to_save_modifiers(Attribute.WISDOM)
        self.assertEqual(will_save.modifier.value, -2)
        self.assertEqual(len(will_save.applicable_attributes), 1)
        self.assertEqual(will_save.applicable_attributes[0], Attribute.WISDOM)

    def test_add_attribute_to_save_adds_additional_modifiers(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 5), Attribute(Attribute.DEXTERITY, 20)], [Fighter(3)])
        will_save = Will(actor)
        self.assertEqual(will_save.modifier.value, -2)
        self.assertEqual(will_save.applicable_attributes[0], Attribute.WISDOM)

        will_save.add_attribute_to_save_modifiers(Attribute.DEXTERITY)
        self.assertEqual(will_save.modifier.value, 3)
        self.assertEqual(len(will_save.applicable_attributes), 2)
        self.assertEqual(will_save.applicable_attributes[0], Attribute.WISDOM)
        self.assertEqual(will_save.applicable_attributes[1], Attribute.DEXTERITY)

    def test_save_includes_audit_trail(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 2), Attribute(Attribute.DEXTERITY, 20)], [Fighter(7)])
        will_save = Will(actor)
        self.assertEqual(
            will_save.modifier.audit_explanation,
            '+2, Level 7 Fighter class bonus. -4, Wisdom ability score of 2. '
        )
