__author__ = 'John Mullins'

import unittest
from saving_throw import SavingThrow
from actor import Actor
from attribute import Attribute
from character_classes.fighter import Fighter


class TestSavingThrow(unittest.TestCase):

    def test_saving_throw_requires_valid_name(self):
        with self.assertRaisesRegexp(ValueError, 'not a valid name is not a valid saving throw name'):
            SavingThrow(None, 'not a valid name')

    def test_fortitude_save_includes_con_bonus(self):
        actor = Actor('John', [Attribute(Attribute.CONSTITUTION, 14)], [Fighter(1)])
        fort_save = SavingThrow(actor, SavingThrow.FORTITUDE)
        self.assertEqual(fort_save.modifier.value, 4)

    def test_reflex_save_includes_dex_bonus(self):
        actor = Actor('John', [Attribute(Attribute.DEXTERITY, 17)], [Fighter(3)])
        reflex_save = SavingThrow(actor, SavingThrow.REFLEX)
        self.assertEqual(reflex_save.modifier.value, 4)

    def test_will_save_includes_wis_bonus(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 5)], [Fighter(3)])
        will_save = SavingThrow(actor, SavingThrow.WILL)
        self.assertEqual(will_save.modifier.value, -2)

    def test_add_attribute_to_save_bonus_ignores_duplicates(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 5)], [Fighter(3)])
        will_save = SavingThrow(actor, SavingThrow.WILL)
        self.assertEqual(will_save.modifier.value, -2)

        will_save.add_attribute_to_save_modifiers(Attribute.WISDOM)
        self.assertEqual(will_save.modifier.value, -2)
        self.assertEqual(len(will_save.attributes_with_modifiers), 1)

    def test_add_attribute_to_save_adds_additional_modifiers(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 5), Attribute(Attribute.DEXTERITY, 20)], [Fighter(3)])
        will_save = SavingThrow(actor, SavingThrow.WILL)
        self.assertEqual(will_save.modifier.value, -2)

        will_save.add_attribute_to_save_modifiers(Attribute.DEXTERITY)
        self.assertEqual(will_save.modifier.value, 3)
        self.assertEqual(len(will_save.attributes_with_modifiers), 2)

    def test_save_includes_audit_trail(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 2), Attribute(Attribute.DEXTERITY, 20)], [Fighter(7)])
        will_save = SavingThrow(actor, SavingThrow.WILL)
        self.assertEqual(
            will_save.modifier.audit_explanation,
            '+2, Level 7 Fighter class bonus. -4, Wisdom ability score of 2. '
        )
