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
            self.assertEqual(rogue.get_fortitude_save().value, per_level_bonus[1])

    def test_rogue_reflex_save_uses_fast_progression(self):
        for per_level_bonus in TestCharacterClass.get_fast_save_per_level():
            rogue = Rogue(per_level_bonus[0])
            self.assertEqual(rogue.get_reflex_save().value, per_level_bonus[1])

    def test_rogue_will_save_uses_slow_progression(self):
        for per_level_bonus in TestCharacterClass.get_slow_save_per_level():
            rogue = Rogue(per_level_bonus[0])
            self.assertEqual(rogue.get_will_save().value, per_level_bonus[1])

    def test_fighter_class_named_fighter(self):
        rogue = Rogue(12)
        self.assertEqual(rogue.name, 'Rogue')

    def test_rogue_fortitude_save_includes_audit(self):
        rogue = Rogue(17)
        self.assertEqual(rogue.get_fortitude_save().audit_explanation, '+5, Level 17 Rogue class bonus. ')

    def test_rogue_reflex_save_includes_audit(self):
        rogue = Rogue(16)
        self.assertEqual(rogue.get_reflex_save().audit_explanation, '+10, Level 16 Rogue class bonus. ')

    def test_rogue_will_save_includes_audit(self):
        rogue = Rogue(15)
        self.assertEqual(rogue.get_will_save().audit_explanation, '+5, Level 15 Rogue class bonus. ')
