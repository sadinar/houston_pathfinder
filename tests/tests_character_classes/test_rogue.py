__author__ = 'John Mullins'

import unittest
from character_classes.rogue import Rogue
from tests.test_character_class import TestCharacterClass


class TestRogue(unittest.TestCase):

    def test_rogue_has_level(self):
        rogue = Rogue(12)
        self.assertEqual(rogue.level, 12)

    def test_rogue_uses_medium_attack_progression(self):
        for per_level_bonus in TestCharacterClass.get_medium_attack_bonus_per_level():
            rogue = Rogue(per_level_bonus[0])
            self.assertEqual(rogue.get_base_attack_bonus(), per_level_bonus[1])

    def test_rogue_fortitude_save_uses_slow_progression(self):
        for per_level_bonus in TestCharacterClass.get_slow_save_per_level():
            rogue = Rogue(per_level_bonus[0])
            self.assertEqual(rogue.get_fortitude_save(), per_level_bonus[1])

    def test_rogue_reflex_save_uses_fast_progression(self):
        for per_level_bonus in TestCharacterClass.get_fast_save_per_level():
            rogue = Rogue(per_level_bonus[0])
            self.assertEqual(rogue.get_reflex_save(), per_level_bonus[1])

    def test_rogue_will_save_uses_slow_progression(self):
        for per_level_bonus in TestCharacterClass.get_slow_save_per_level():
            rogue = Rogue(per_level_bonus[0])
            self.assertEqual(rogue.get_will_save(), per_level_bonus[1])

    def test_fighter_class_named_fighter(self):
        rogue = Rogue(12)
        self.assertEqual(rogue.name, 'Rogue')
