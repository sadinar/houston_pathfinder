__author__ = 'John Mullins'

import unittest
from character_class import CharacterClass


class TestCharacterClass(unittest.TestCase):

    def test_character_class_is_abstract(self):
        expected_message = "Can't instantiate abstract class CharacterClass with abstract methods "
        "get_base_attack_bonus, get_fortitude_save, get_reflex_save, get_will_save"

        with self.assertRaisesRegexp(TypeError, expected_message):
            CharacterClass()

    def test_get_fast_progression_attack_bonus_uses_fast_bonus(self):
        for per_level_bonus in self.get_fast_attack_bonus_per_level():
            self.assertEqual(per_level_bonus[1], CharacterClass._get_fast_progression_attack_bonus(per_level_bonus[0]))

    def test_get_medium_progression_attack_bonus_uses_medium_bonus(self):
        for per_level_bonus in self.get_medium_attack_bonus_per_level():
            self.assertEqual(
                per_level_bonus[1],
                CharacterClass._get_medium_progression_attack_bonus(per_level_bonus[0])
            )

    def test_get_slow_progression_attack_bonus_uses_slow_bonus(self):
        for per_level_bonus in self.get_slow_attack_bonus_per_level():
            self.assertEqual(per_level_bonus[1], CharacterClass._get_slow_progression_attack_bonus(per_level_bonus[0]))

    def test_get_fast_progression_save_returns_fast_save(self):
        for per_level_bonus in self.get_fast_save_per_level():
            self.assertEqual(per_level_bonus[1], CharacterClass._get_fast_progression_save(per_level_bonus[0]))

    def test_get_slow_progression_save_returns_slow_save(self):
        for per_level_bonus in self.get_slow_save_per_level():
            self.assertEqual(per_level_bonus[1], CharacterClass._get_slow_progression_save(per_level_bonus[0]))

    @staticmethod
    def get_fast_attack_bonus_per_level():
        # inner list in [level, bonus] format
        return [
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 4],
            [5, 5],
            [6, 6],
            [7, 7],
            [8, 8],
            [9, 9],
            [10, 10],
            [11, 11],
            [12, 12],
            [13, 13],
            [14, 14],
            [15, 15],
            [16, 16],
            [17, 17],
            [18, 18],
            [19, 19],
            [20, 20],
        ]

    @staticmethod
    def get_medium_attack_bonus_per_level():
        # inner list in [level, bonus] format
        return [
            [1, 0],
            [2, 1],
            [3, 2],
            [4, 3],
            [5, 3],
            [6, 4],
            [7, 5],
            [8, 6],
            [9, 6],
            [10, 7],
            [11, 8],
            [12, 9],
            [13, 9],
            [14, 10],
            [15, 11],
            [16, 12],
            [17, 12],
            [18, 13],
            [19, 14],
            [20, 15],
        ]

    @staticmethod
    def get_slow_attack_bonus_per_level():
        # inner list in [level, bonus] format
        return [
            [1, 0],
            [2, 1],
            [3, 1],
            [4, 2],
            [5, 2],
            [6, 3],
            [7, 3],
            [8, 4],
            [9, 4],
            [10, 5],
            [11, 5],
            [12, 6],
            [13, 6],
            [14, 7],
            [15, 7],
            [16, 8],
            [17, 8],
            [18, 9],
            [19, 9],
            [20, 10],
        ]

    @staticmethod
    def get_fast_save_per_level():
        # inner list in [level, bonus] format
        return [
            [1, 2],
            [2, 3],
            [3, 3],
            [4, 4],
            [5, 4],
            [6, 5],
            [7, 5],
            [8, 6],
            [9, 6],
            [10, 7],
            [11, 7],
            [12, 8],
            [13, 8],
            [14, 9],
            [15, 9],
            [16, 10],
            [17, 10],
            [18, 11],
            [19, 11],
            [20, 12],
        ]

    @staticmethod
    def get_slow_save_per_level():
        # inner list in [level, bonus] format
        return [
            [1, 0],
            [2, 0],
            [3, 1],
            [4, 1],
            [5, 1],
            [6, 2],
            [7, 2],
            [8, 2],
            [9, 3],
            [10, 3],
            [11, 3],
            [12, 4],
            [13, 4],
            [14, 4],
            [15, 5],
            [16, 5],
            [17, 5],
            [18, 6],
            [19, 6],
            [20, 6],
        ]
