__author__ = 'John Mullins'

import unittest
from saving_throws.fortitude import Fortitude
from actor import Actor
from attribute import Attribute
from character_classes.fighter import Fighter


class TestFortitude(unittest.TestCase):

    def test_fortitude_save_includes_con_bonus(self):
        actor = Actor('John', [Attribute(Attribute.CONSTITUTION, 14)], [Fighter(1)])
        fort_save = Fortitude(actor)
        self.assertEqual(fort_save.modifier.value, 4)
        self.assertEqual(
            fort_save.modifier.audit_explanation,
            '+2, Level 1 Fighter class bonus. +2, Constitution ability score of 14. '
        )

    def test_fortitude_save_named_correctly(self):
        actor = Actor('John', [Attribute(Attribute.CONSTITUTION, 8)], [Fighter(4)])
        fort_save = Fortitude(actor)
        self.assertEqual(fort_save.name, 'Fortitude')
