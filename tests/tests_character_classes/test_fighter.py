__author__ = 'John Mullins'

import unittest
from character_classes.fighter import Fighter
from character_class import CharacterClass

class TestFighter(unittest.TestCase):
    def test_fighter_has_level(self):
        fighter = Fighter(2)
        self.assertEqual(fighter.level, 2)

    def test_fighter_uses_fast_attack_progression(self):
        fighter = Fighter(1)
        self.assertEqual(fighter.get_base_attack_bonus(), CharacterClass._get_fast_progression_attack_bonus(1))
        fighter = Fighter(7)
        self.assertEqual(fighter.get_base_attack_bonus(), CharacterClass._get_fast_progression_attack_bonus(7))
        fighter = Fighter(20)
        self.assertEqual(fighter.get_base_attack_bonus(), CharacterClass._get_fast_progression_attack_bonus(20))

    def test_fighter_fortitude_save_uses_fast_progression(self):
        fighter = Fighter(1)
        self.assertEqual(fighter.get_fortitude_save(), CharacterClass._get_fast_progression_save(1))
        fighter = Fighter(8)
        self.assertEqual(fighter.get_fortitude_save(), CharacterClass._get_fast_progression_save(8))
        fighter = Fighter(20)
        self.assertEqual(fighter.get_fortitude_save(), CharacterClass._get_fast_progression_save(20))

    def test_fighter_reflex_save_uses_slow_progression(self):
        fighter = Fighter(1)
        self.assertEqual(fighter.get_reflex_save(), CharacterClass._get_slow_progression_save(1))
        fighter = Fighter(13)
        self.assertEqual(fighter.get_reflex_save(), CharacterClass._get_slow_progression_save(13))
        fighter = Fighter(20)
        self.assertEqual(fighter.get_reflex_save(), CharacterClass._get_slow_progression_save(20))

    def test_fighter_will_save_uses_slow_progression(self):
        fighter = Fighter(1)
        self.assertEqual(fighter.get_will_save(), CharacterClass._get_slow_progression_save(1))
        fighter = Fighter(3)
        self.assertEqual(fighter.get_will_save(), CharacterClass._get_slow_progression_save(3))
        fighter = Fighter(20)
        self.assertEqual(fighter.get_will_save(), CharacterClass._get_slow_progression_save(20))
