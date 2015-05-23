__author__ = 'John Mullins'

import unittest
from actor import Actor
from attribute import Attribute
from character_classes.fighter import Fighter
from character_classes.rogue import Rogue


class TestActor(unittest.TestCase):

    def test_actor_has_name(self):
        actor = Actor('My Name', [], [])
        self.assertEqual(actor.name, 'My Name')

    def test_actor_has_attributes(self):
        strength = Attribute(Attribute.STRENGTH, 18)
        constitution = Attribute(Attribute.CONSTITUTION, 16)
        actor = Actor('Test Fighter Guy', [strength, constitution], [])
        self.assertEqual(actor.base_attributes[Attribute.STRENGTH].score, 18)
        self.assertEqual(actor.base_attributes[Attribute.STRENGTH].name, 'Strength')
        self.assertEqual(actor.base_attributes[Attribute.CONSTITUTION].score, 16)
        self.assertEqual(actor.base_attributes[Attribute.CONSTITUTION].name, 'Constitution')

    def test_get_attack_bonus_requires_list_of_Attributes(self):
        strength = Attribute(Attribute.STRENGTH, 14)
        actor = Actor('Test Actor Dude', [strength], [])
        with self.assertRaisesRegexp(
                ValueError,
                'A list of attributes, possibly empty, must be provided to calculate attack bonus'
        ):
            actor.get_attack_bonus(Attribute.STRENGTH), strength.get_attribute_modifier()

    def test_actor_includes_attributes_in_attack_bonus(self):
        strength = Attribute(Attribute.STRENGTH, 14)
        actor = Actor('Test Actor Dude', [strength], [])
        self.assertEqual(actor.get_attack_bonus([Attribute.STRENGTH]), strength.get_attribute_modifier())

    def test_actor_includes_class_base_attack_bonus_in_attack_bonus(self):
        fighter = Fighter(16)
        actor = Actor('Test Actor Dude', [], [fighter])
        self.assertEqual(actor.get_attack_bonus([]), fighter.get_base_attack_bonus())

    def test_actor_combines_class_and_attribute_bonus_during_attack_bonus_calculation(self):
        fighter = Fighter(16)
        strength = Attribute(Attribute.STRENGTH, 19)
        actor = Actor('Test Actor Dude', [strength], [fighter])
        self.assertEqual(
            actor.get_attack_bonus([Attribute.STRENGTH]),
            fighter.get_base_attack_bonus() + strength.get_attribute_modifier()
        )

    def test_fortitude_save_includes_constitution_bonus(self):
        constitution = Attribute(Attribute.CONSTITUTION, 19)
        actor = Actor('Test Actor Dude', [constitution], [])
        self.assertEqual(actor.get_fortitude_save(), constitution.get_attribute_modifier())

    def test_fortitude_save_includes_class_bonus(self):
        fighter = Fighter(14)
        actor = Actor('Test Actor Dude', [], [fighter])
        self.assertEqual(actor.get_fortitude_save(), fighter.get_fortitude_save())

    def test_fortitude_save_combines_constitution_and_class_bonus(self):
        constitution = Attribute(Attribute.CONSTITUTION, 17)
        rogue = Rogue(19)
        actor = Actor('Test Rogue With Rouge', [constitution], [rogue])
        self.assertEqual(
            actor.get_fortitude_save(),
            rogue.get_fortitude_save() + constitution.get_attribute_modifier()
        )

    def test_reflex_save_includes_dexterity_bonus(self):
        dexterity = Attribute(Attribute.DEXTERITY, 13)
        actor = Actor('Test Actor Dude', [dexterity], [])
        self.assertEqual(actor.get_reflex_save(), dexterity.get_attribute_modifier())

    def test_reflex_save_includes_class_bonus(self):
        rogue = Rogue(15)
        actor = Actor('Test Actor Dude', [], [rogue])
        self.assertEqual(actor.get_reflex_save(), rogue.get_reflex_save())

    def test_reflex_save_combines_dexterity_and_class_bonus(self):
        dexterity = Attribute(Attribute.DEXTERITY, 13)
        rogue = Rogue(17)
        actor = Actor('Test Rogue With Rouge', [dexterity], [rogue])
        self.assertEqual(
            actor.get_reflex_save(),
            rogue.get_reflex_save() + dexterity.get_attribute_modifier()
        )

    def test_will_save_includes_wisdom_bonus(self):
        wisdom = Attribute(Attribute.WISDOM, 24)
        actor = Actor('Test Actor Dude', [wisdom], [])
        self.assertEqual(actor.get_will_save(), wisdom.get_attribute_modifier())

    def test_will_save_includes_class_bonus(self):
        rogue = Rogue(19)
        actor = Actor('Test Actor Dude', [], [rogue])
        self.assertEqual(actor.get_will_save(), rogue.get_will_save())

    def test_will_save_combines_wisdom_and_class_bonus(self):
        wisdom = Attribute(Attribute.WISDOM, 21)
        rogue = Rogue(20)
        actor = Actor('Test Rogue With Rouge', [wisdom], [rogue])
        self.assertEqual(
            actor.get_will_save(),
            rogue.get_will_save() + wisdom.get_attribute_modifier()
        )
