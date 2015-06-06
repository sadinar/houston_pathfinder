__author__ = 'John Mullins'

import unittest
from character_classes.fighter import Fighter
from tests.test_character_class import TestCharacterClass


class TestFighter(unittest.TestCase):

    def test_fighter_has_level(self):
        fighter = Fighter(2)
        self.assertEqual(2, fighter.level)

    def test_fighter_uses_fast_attack_progression(self):
        for per_level_bonus in TestCharacterClass.get_fast_attack_bonus_per_level():
            fighter = Fighter(per_level_bonus[0])
            self.assertEqual(per_level_bonus[1], fighter.get_base_attack_bonus())

    def test_fighter_fortitude_save_uses_fast_progression(self):
        for per_level_bonus in TestCharacterClass.get_fast_save_per_level():
            fighter = Fighter(per_level_bonus[0])
            self.assertEqual(per_level_bonus[1], fighter.get_fortitude_save().value)

    def test_fighter_reflex_save_uses_slow_progression(self):
        for per_level_bonus in TestCharacterClass.get_slow_save_per_level():
            fighter = Fighter(per_level_bonus[0])
            self.assertEqual(per_level_bonus[1], fighter.get_reflex_save().value)

    def test_fighter_will_save_uses_slow_progression(self):
        for per_level_bonus in TestCharacterClass.get_slow_save_per_level():
            fighter = Fighter(per_level_bonus[0])
            self.assertEqual(per_level_bonus[1], fighter.get_will_save().value)

    def test_fighter_class_named_fighter(self):
        fighter = Fighter(14)
        self.assertEqual('Fighter', fighter.name)

    def test_fighter_level_below_zero_not_allowed(self):
        with self.assertRaisesRegexp(ValueError, 'Character levels must be numbers from 1 to 20'):
            Fighter(0)

    def test_fighter_level_above_twenty_not_allowed(self):
        with self.assertRaisesRegexp(ValueError, 'Character levels must be numbers from 1 to 20'):
            Fighter(21)

    def test_fighter_fortitude_save_includes_audit(self):
        fighter = Fighter(20)
        self.assertEqual('+12, Level 20 Fighter class bonus. ', fighter.get_fortitude_save().audit_explanation)

    def test_fighter_reflex_save_includes_audit(self):
        fighter = Fighter(19)
        self.assertEqual('+6, Level 19 Fighter class bonus. ', fighter.get_reflex_save().audit_explanation)

    def test_fighter_will_save_includes_audit(self):
        fighter = Fighter(18)
        self.assertEqual('+6, Level 18 Fighter class bonus. ', fighter.get_will_save().audit_explanation)
