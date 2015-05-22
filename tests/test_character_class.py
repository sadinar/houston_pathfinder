__author__ = 'John Mullins'

import unittest
from character_class import CharacterClass

class TestCharacterClass(unittest.TestCase):
    def test_character_class_is_abstract(self):
        expectedMessage = "Can't instantiate abstract class CharacterClass with abstract methods "
        "get_base_attack_bonus, get_fortitude_save, get_reflex_save, get_will_save"

        with self.assertRaisesRegexp(TypeError, expectedMessage):
            CharacterClass()

    def test_get_fast_progression_attack_bonus_uses_fast_bonus(self):
        self.assertEqual(CharacterClass._get_fast_progression_attack_bonus(1), 1)
        self.assertEqual(CharacterClass._get_fast_progression_attack_bonus(9), 9)
        self.assertEqual(CharacterClass._get_fast_progression_attack_bonus(20), 20)

    def test_get_medium_progression_attack_bonus_uses_medium_bonus(self):
        self.assertEqual(CharacterClass._get_medium_progression_attack_bonus(1), 0)
        self.assertEqual(CharacterClass._get_medium_progression_attack_bonus(9), 6)
        self.assertEqual(CharacterClass._get_medium_progression_attack_bonus(20), 15)

    def test_get_slow_progression_attack_bonus_uses_slow_bonus(self):
        self.assertEqual(CharacterClass._get_slow_progression_attack_bonus(1), 0)
        self.assertEqual(CharacterClass._get_slow_progression_attack_bonus(9), 4)
        self.assertEqual(CharacterClass._get_slow_progression_attack_bonus(20), 10)

    def test_get_fast_progression_save_returns_fast_save(self):
        self.assertEqual(CharacterClass._get_fast_progression_save(1), 2)
        self.assertEqual(CharacterClass._get_fast_progression_save(9), 6)
        self.assertEqual(CharacterClass._get_fast_progression_save(20), 12)

    def test_get_slow_progression_save_returns_slow_save(self):
        self.assertEqual(CharacterClass._get_slow_progression_save(1), 0)
        self.assertEqual(CharacterClass._get_slow_progression_save(9), 3)
        self.assertEqual(CharacterClass._get_slow_progression_save(20), 6)
