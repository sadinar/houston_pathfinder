__author__ = 'John Mullins'

import unittest
from character_classes.fighter import Fighter
from tests.test_character_class import TestCharacterClass


class TestFighter(unittest.TestCase):

    def test_fighter_has_level(self):
        fighter = Fighter(2)
        self.assertEqual(fighter.level, 2)

    def test_fighter_uses_fast_attack_progression(self):
        for per_level_bonus in TestCharacterClass.get_fast_attack_bonus_per_level():
            fighter = Fighter(per_level_bonus[0])
            self.assertEqual(fighter.get_base_attack_bonus(), per_level_bonus[1])

    def test_fighter_fortitude_save_uses_fast_progression(self):
        for per_level_bonus in TestCharacterClass.get_fast_save_per_level():
            fighter = Fighter(per_level_bonus[0])
            self.assertEqual(fighter.get_fortitude_save(), per_level_bonus[1])

    def test_fighter_reflex_save_uses_slow_progression(self):
        for per_level_bonus in TestCharacterClass.get_slow_save_per_level():
            fighter = Fighter(per_level_bonus[0])
            self.assertEqual(fighter.get_reflex_save(), per_level_bonus[1])

    def test_fighter_will_save_uses_slow_progression(self):
        for per_level_bonus in TestCharacterClass.get_slow_save_per_level():
            fighter = Fighter(per_level_bonus[0])
            self.assertEqual(fighter.get_will_save(), per_level_bonus[1])

    def test_fighter_class_named_fighter(self):
        fighter = Fighter(14)
        self.assertEqual(fighter.name, 'Fighter')

    def test_fighter_level_below_zero_not_allowed(self):
        with self.assertRaisesRegexp(ValueError, 'Character levels must be numbers from 1 to 20'):
            Fighter(0)

    def test_fighter_level_above_twenty_not_allowed(self):
        with self.assertRaisesRegexp(ValueError, 'Character levels must be numbers from 1 to 20'):
            Fighter(21)
