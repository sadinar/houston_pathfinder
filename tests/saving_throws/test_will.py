__author__ = 'John Mullins'

import unittest
from saving_throws.will import Will
from actor import Actor
from attribute import Attribute
from character_classes.rogue import Rogue


class TestWill(unittest.TestCase):

    def test_will_save_includes_wis_bonus(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 16)], [Rogue(11)])
        will_save = Will(actor)
        self.assertEqual(will_save.modifier.value, 6)
        self.assertEqual(
            will_save.modifier.audit_explanation,
            '+3, Level 11 Rogue class bonus. +3, Wisdom ability score of 16. '
        )

    def test_will_save_named_correctly(self):
        actor = Actor('John', [Attribute(Attribute.WISDOM, 10)], [Rogue(15)])
        will_save = Will(actor)
        self.assertEqual(will_save.name, 'Will')
