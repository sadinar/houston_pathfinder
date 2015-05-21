__author__ = 'John'

import unittest
from actor import Actor
from attribute import Attribute

class TestActor(unittest.TestCase):
    def test_actor_has_name(self):
        actor = Actor('My Name', [])
        self.assertEqual(actor.name, 'My Name')

    def test_actor_has_attributes(self):
        strength = Attribute('Strength', 18)
        constitution = Attribute('Constitution', 16)
        actor = Actor('Test Fighter Guy', [strength, constitution])
        self.assertEqual(actor.base_attributes['Strength'].score, 18)
        self.assertEqual(actor.base_attributes['Strength'].name, 'Strength')
        self.assertEqual(actor.base_attributes['Constitution'].score, 16)
        self.assertEqual(actor.base_attributes['Constitution'].name, 'Constitution')

    def test_actor_calculates_attack_bonus(self):
        strength = Attribute('Strength', 18)
        constitution = Attribute('Constitution', 16)
        actor = Actor('Test Fighter Guy', [strength, constitution])
        self.assertEqual(actor.get_attack_bonus(['Strength']), 17)
