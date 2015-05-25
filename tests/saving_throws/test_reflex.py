__author__ = 'John Mullins'

import unittest
from saving_throws.reflex import Reflex
from actor import Actor
from attribute import Attribute
from character_classes.rogue import Rogue


class TestReflex(unittest.TestCase):

    def test_reflex_save_includes_dex_bonus(self):
        actor = Actor('John', [Attribute(Attribute.DEXTERITY, 17)], [Rogue(8)])
        reflex_save = Reflex(actor)
        self.assertEqual(reflex_save.modifier.value, 9)
        self.assertEqual(
            reflex_save.modifier.audit_explanation,
            '+6, Level 8 Rogue class bonus. +3, Dexterity ability score of 17. '
        )

    def test_reflex_save_named_correctly(self):
        actor = Actor('John', [Attribute(Attribute.DEXTERITY, 9)], [Rogue(9)])
        reflex_save = Reflex(actor)
        self.assertEqual(reflex_save.name, 'Reflex')
