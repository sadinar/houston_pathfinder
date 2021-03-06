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
            '+3, Level 11 Rogue class bonus. +3, Wisdom ability score of 16. ',
            will_save.get_modifier().audit_explanation
        )

    def test_will_save_named_correctly(self):
        will_save = SavingThrow(SavingThrow.WILL, [], None)
        self.assertEqual('Will', will_save.name)

    def test_reflex_save_includes_dex_bonus(self):
        actor = Actor('John', [Attribute(Attribute.DEXTERITY, 17)], [Rogue(8)])
        reflex_save = actor._saving_throws[SavingThrow.REFLEX]
        self.assertEqual(reflex_save.get_modifier().value, 9)
        self.assertEqual(
            '+6, Level 8 Rogue class bonus. +3, Dexterity ability score of 17. ',
            reflex_save.get_modifier().audit_explanation
        )

    def test_reflex_save_named_correctly(self):
        reflex_save = SavingThrow(SavingThrow.REFLEX, [], None)
        self.assertEqual('Reflex', reflex_save.name)

    def test_fortitude_save_includes_con_bonus(self):
        actor = Actor('John', [Attribute(Attribute.CONSTITUTION, 14)], [Fighter(1)])
        fort_save = actor._saving_throws[SavingThrow.FORTITUDE]
        self.assertEqual(4, fort_save.get_modifier().value)
        self.assertEqual(
            '+2, Level 1 Fighter class bonus. +2, Constitution ability score of 14. ',
            fort_save.get_modifier().audit_explanation
        )

    def test_fortitude_save_named_correctly(self):
        fort_save = SavingThrow(SavingThrow.FORTITUDE, [], None)
        self.assertEqual('Fortitude', fort_save.name)

    def test_add_attribute_adds_requested_attribute(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 5)], [Fighter(3)])
        will_save = actor._saving_throws[SavingThrow.WILL]
        self.assertEqual(-2, will_save.get_modifier().value)
        self.assertEqual(1, len(will_save._attributes))
        self.assertIsNotNone(will_save._attributes[SavingThrow.BASE_ATTRIBUTES[SavingThrow.WILL]])

        will_save.add_attribute(Attribute(Attribute.STRENGTH, 39))
        self.assertEqual(12, will_save.get_modifier().value)
        self.assertEqual(2, len(will_save._attributes))
        self.assertIsNotNone(will_save._attributes[SavingThrow.BASE_ATTRIBUTES[SavingThrow.WILL]])
        self.assertIsNotNone(will_save._attributes[Attribute.STRENGTH])

    def test_add_attribute_replaces_original_when_duplicate_name_passed(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 5)], [Fighter(3)])
        will_save = actor._saving_throws[SavingThrow.WILL]
        self.assertEqual(-2, will_save.get_modifier().value)
        self.assertEqual(1, len(will_save._attributes))
        self.assertIsNotNone(will_save._attributes[SavingThrow.BASE_ATTRIBUTES[SavingThrow.WILL]])

        will_save.add_attribute(Attribute(Attribute.WISDOM, 15))
        self.assertEqual(3, will_save.get_modifier().value)
        self.assertEqual(1, len(will_save._attributes))
        self.assertIsNotNone(will_save._attributes[SavingThrow.BASE_ATTRIBUTES[SavingThrow.WILL]])

    def test_save_includes_audit_trail(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 2), Attribute(Attribute.DEXTERITY, 20)], [Fighter(7)])
        will_save = actor._saving_throws[SavingThrow.WILL]
        self.assertEqual(
            '+2, Level 7 Fighter class bonus. -4, Wisdom ability score of 2. ',
            will_save.get_modifier().audit_explanation
        )

    def test_remove_attribute_no_op_for_missing_attribute(self):
        actor = Actor('John', [Attribute(Attribute.CONSTITUTION, 10)], [Fighter(9)])
        fort_save = actor._saving_throws[SavingThrow.FORTITUDE]
        fort_save.remove_attribute(Attribute.DEXTERITY)
        self.assertEqual(6, fort_save.get_modifier().value)
        self.assertEqual(1, len(fort_save._attributes))
        self.assertIsNotNone(fort_save._attributes[SavingThrow.BASE_ATTRIBUTES[SavingThrow.FORTITUDE]])

    def test_saving_throw_rejects_bad_name(self):
        with self.assertRaisesRegexp(ValueError, 'not a name is not a valid saving throw name'):
            SavingThrow('not a name', {}, {})
