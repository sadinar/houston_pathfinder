__author__ = 'John Mullins'

import unittest
from actor import Actor
from attribute import Attribute

class TestActor(unittest.TestCase):
    def test_actor_has_name(self):
        actor = Actor('My Name', [])
        self.assertEqual(actor.name, 'My Name')

    def test_actor_has_attributes(self):
        strength = Attribute(Attribute.STRENGTH, 18)
        constitution = Attribute(Attribute.CONSTITUTION, 16)
        actor = Actor('Test Fighter Guy', [strength, constitution])
        self.assertEqual(actor.base_attributes[Attribute.STRENGTH].score, 18)
        self.assertEqual(actor.base_attributes[Attribute.STRENGTH].name, 'Strength')
        self.assertEqual(actor.base_attributes[Attribute.CONSTITUTION].score, 16)
        self.assertEqual(actor.base_attributes[Attribute.CONSTITUTION].name, 'Constitution')

    def test_actor_calculates_attack_bonus(self):
        strength = Attribute(Attribute.STRENGTH, 18)
        constitution = Attribute(Attribute.CONSTITUTION, 16)
        actor = Actor('Test Fighter Guy', [strength, constitution])
        self.assertEqual(actor.get_attack_bonus([Attribute.STRENGTH]), 17)
