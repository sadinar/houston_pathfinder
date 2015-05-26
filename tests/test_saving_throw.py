__author__ = 'John Mullins'

import unittest
from actor import Actor
from attribute import Attribute
from character_classes.fighter import Fighter
from character_classes.rogue import Rogue
from saving_throw import SavingThrow


class TestSavingThrow(unittest.TestCase):

    def test_will_save_includes_wis_bonus(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 16)], [Rogue(11)])
        will_save = actor._saving_throws[SavingThrow.WILL]
        self.assertEqual(will_save.get_modifier().value, 6)
        self.assertEqual(
            will_save.get_modifier().audit_explanation,
            '+3, Level 11 Rogue class bonus. +3, Wisdom ability score of 16. '
        )

    def test_will_save_named_correctly(self):
        will_save = SavingThrow(SavingThrow.WILL, [], None)
        self.assertEqual(will_save.name, 'Will')

    def test_reflex_save_includes_dex_bonus(self):
        actor = Actor('John', [Attribute(Attribute.DEXTERITY, 17)], [Rogue(8)])
        reflex_save = actor._saving_throws[SavingThrow.REFLEX]
        self.assertEqual(reflex_save.get_modifier().value, 9)
        self.assertEqual(
            reflex_save.get_modifier().audit_explanation,
            '+6, Level 8 Rogue class bonus. +3, Dexterity ability score of 17. '
        )

    def test_reflex_save_named_correctly(self):
        reflex_save = SavingThrow(SavingThrow.REFLEX, [], None)
        self.assertEqual(reflex_save.name, 'Reflex')

    def test_fortitude_save_includes_con_bonus(self):
        actor = Actor('John', [Attribute(Attribute.CONSTITUTION, 14)], [Fighter(1)])
        fort_save = actor._saving_throws[SavingThrow.FORTITUDE]
        self.assertEqual(fort_save.get_modifier().value, 4)
        self.assertEqual(
            fort_save.get_modifier().audit_explanation,
            '+2, Level 1 Fighter class bonus. +2, Constitution ability score of 14. '
        )

    def test_fortitude_save_named_correctly(self):
        fort_save = SavingThrow(SavingThrow.FORTITUDE, [], None)
        self.assertEqual(fort_save.name, 'Fortitude')

    def test_add_attribute_to_save_bonus_ignores_duplicates(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 5)], [Fighter(3)])
        will_save = actor._saving_throws[SavingThrow.WILL]
        self.assertEqual(will_save.get_modifier().value, -2)
        self.assertEqual(len(will_save._attributes), 1)
        self.assertIsNotNone(will_save._attributes[SavingThrow.BASE_ATTRIBUTES[SavingThrow.WILL]])

        will_save.add_attribute_to_save_modifiers(Attribute(Attribute.WISDOM, 15))
        self.assertEqual(will_save.get_modifier().value, -2)
        self.assertEqual(len(will_save._attributes), 1)
        self.assertIsNotNone(will_save._attributes[SavingThrow.BASE_ATTRIBUTES[SavingThrow.WILL]])

    def test_save_includes_audit_trail(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 2), Attribute(Attribute.DEXTERITY, 20)], [Fighter(7)])
        will_save = actor._saving_throws[SavingThrow.WILL]
        self.assertEqual(
            will_save.get_modifier().audit_explanation,
            '+2, Level 7 Fighter class bonus. -4, Wisdom ability score of 2. '
        )
