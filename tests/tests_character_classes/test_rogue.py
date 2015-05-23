__author__ = 'John Mullins'

import unittest
from character_classes.rogue import Rogue
from character_class import CharacterClass

class Testrogue(unittest.TestCase):
    def test_rogue_has_level(self):
        rogue = Rogue(12)
        self.assertEqual(rogue.level, 12)

    def test_rogue_uses_medium_attack_progression(self):
        rogue = Rogue(1)
        self.assertEqual(rogue.get_base_attack_bonus(), CharacterClass._get_medium_progression_attack_bonus(1))
        rogue = Rogue(5)
        self.assertEqual(rogue.get_base_attack_bonus(), CharacterClass._get_medium_progression_attack_bonus(5))
        rogue = Rogue(20)
        self.assertEqual(rogue.get_base_attack_bonus(), CharacterClass._get_medium_progression_attack_bonus(20))

    def test_rogue_fortitude_save_uses_slow_progression(self):
        rogue = Rogue(1)
        self.assertEqual(rogue.get_fortitude_save(), CharacterClass._get_slow_progression_save(1))
        rogue = Rogue(2)
        self.assertEqual(rogue.get_fortitude_save(), CharacterClass._get_slow_progression_save(2))
        rogue = Rogue(20)
        self.assertEqual(rogue.get_fortitude_save(), CharacterClass._get_slow_progression_save(20))

    def test_rogue_reflex_save_uses_fast_progression(self):
        rogue = Rogue(1)
        self.assertEqual(rogue.get_reflex_save(), CharacterClass._get_fast_progression_save(1))
        rogue = Rogue(13)
        self.assertEqual(rogue.get_reflex_save(), CharacterClass._get_fast_progression_save(13))
        rogue = Rogue(20)
        self.assertEqual(rogue.get_reflex_save(), CharacterClass._get_fast_progression_save(20))

    def test_rogue_will_save_uses_slow_progression(self):
        rogue = Rogue(1)
        self.assertEqual(rogue.get_will_save(), CharacterClass._get_slow_progression_save(1))
        rogue = Rogue(19)
        self.assertEqual(rogue.get_will_save(), CharacterClass._get_slow_progression_save(19))
        rogue = Rogue(20)
        self.assertEqual(rogue.get_will_save(), CharacterClass._get_slow_progression_save(20))
