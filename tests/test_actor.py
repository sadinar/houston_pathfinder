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
        self.assertEqual(actor._attributes[Attribute.STRENGTH].score, 18)
        self.assertEqual(actor._attributes[Attribute.STRENGTH].name, 'Strength')
        self.assertEqual(actor._attributes[Attribute.CONSTITUTION].score, 16)
        self.assertEqual(actor._attributes[Attribute.CONSTITUTION].name, 'Constitution')

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
        self.assertEqual(actor.get_attack_bonus([Attribute.STRENGTH])[0], strength.get_attribute_modifier().value)

    def test_actor_includes_class_base_attack_bonus_in_attack_bonus(self):
        fighter = Fighter(7)
        actor = Actor('Test Actor Dude', [], [fighter])
        self.assertEqual(actor.get_attack_bonus([]), [7, 2])

    def test_actor_combines_class_and_attribute_bonus_during_attack_bonus_calculation(self):
        fighter = Fighter(16)
        strength = Attribute(Attribute.STRENGTH, 19)
        actor = Actor('Test Actor Dude', [strength], [fighter])
        expected_bonuses = [20, 15, 10, 5]
        self.assertEqual(actor.get_attack_bonus([Attribute.STRENGTH]), expected_bonuses)

    def test_fortitude_save_includes_constitution_bonus(self):
        constitution = Attribute(Attribute.CONSTITUTION, 19)
        actor = Actor('Test Actor Dude', [constitution], [])
        self.assertEqual(actor.get_fortitude_save().value, constitution.get_attribute_modifier().value)

    def test_fortitude_save_includes_class_bonus(self):
        fighter = Fighter(14)
        actor = Actor('Test Actor Dude', [], [fighter])
        self.assertEqual(actor.get_fortitude_save().value, fighter.get_fortitude_save().value)

    def test_fortitude_save_combines_constitution_and_class_bonus(self):
        constitution = Attribute(Attribute.CONSTITUTION, 17)
        rogue = Rogue(19)
        actor = Actor('Test Rogue With Rouge', [constitution], [rogue])
        self.assertEqual(
            actor.get_fortitude_save().value,
            rogue.get_fortitude_save().value + constitution.get_attribute_modifier().value
        )

    def test_reflex_save_includes_dexterity_bonus(self):
        dexterity = Attribute(Attribute.DEXTERITY, 13)
        actor = Actor('Test Actor Dude', [dexterity], [])
        self.assertEqual(actor.get_reflex_save().value, dexterity.get_attribute_modifier().value)

    def test_reflex_save_includes_class_bonus(self):
        rogue = Rogue(15)
        actor = Actor('Test Actor Dude', [], [rogue])
        self.assertEqual(actor.get_reflex_save().value, rogue.get_reflex_save().value)

    def test_reflex_save_combines_dexterity_and_class_bonus(self):
        dexterity = Attribute(Attribute.DEXTERITY, 13)
        rogue = Rogue(17)
        actor = Actor('Test Rogue With Rouge', [dexterity], [rogue])
        self.assertEqual(
            actor.get_reflex_save().value,
            rogue.get_reflex_save().value + dexterity.get_attribute_modifier().value
        )

    def test_will_save_includes_wisdom_bonus(self):
        wisdom = Attribute(Attribute.WISDOM, 24)
        actor = Actor('Test Actor Dude', [wisdom], [])
        self.assertEqual(actor.get_will_save().value, wisdom.get_attribute_modifier().value)

    def test_will_save_includes_class_bonus(self):
        rogue = Rogue(19)
        actor = Actor('Test Actor Dude', [], [rogue])
        self.assertEqual(actor.get_will_save().value, rogue.get_will_save().value)

    def test_will_save_combines_wisdom_and_class_bonus(self):
        wisdom = Attribute(Attribute.WISDOM, 21)
        rogue = Rogue(20)
        actor = Actor('Test Rogue With Rouge', [wisdom], [rogue])
        self.assertEqual(
            actor.get_will_save().value,
            rogue.get_will_save().value + wisdom.get_attribute_modifier().value
        )

    def test_actor_combines_multiple_classes_during_attack_calculation(self):
        strength = Attribute(Attribute.STRENGTH, 19)
        fighter = Fighter(3)
        rogue = Rogue(12)
        actor = Actor('Sven', [strength], [fighter, rogue])
        expected_attacks = [16, 11, 6]
        self.assertEqual(actor.get_attack_bonus([Attribute.STRENGTH]), expected_attacks)

    def test_fortitude_save_includes_audit(self):
        constitution = Attribute(Attribute.CONSTITUTION, 22)
        rogue = Rogue(1)
        actor = Actor('Test Rogue With Rouge', [constitution], [rogue])
        self.assertEqual(
            actor.get_fortitude_save().audit_explanation,
            '+0, Level 1 Rogue class bonus. +6, Constitution ability score of 22. '
        )

    def test_reflex_save_includes_audit(self):
        dexterity = Attribute(Attribute.DEXTERITY, 23)
        rogue = Rogue(2)
        actor = Actor('Test Rogue With Rouge', [dexterity], [rogue])
        self.assertEqual(
            actor.get_reflex_save().audit_explanation,
            '+3, Level 2 Rogue class bonus. +6, Dexterity ability score of 23. '
        )

    def test_will_save_includes_audit(self):
        wisdom = Attribute(Attribute.WISDOM, 24)
        rogue = Rogue(3)
        actor = Actor('Test Rogue With Rouge', [wisdom], [rogue])
        self.assertEqual(
            actor.get_will_save().audit_explanation,
            '+1, Level 3 Rogue class bonus. +7, Wisdom ability score of 24. '
        )

    def test_get_base_attribute_score_flags_missing_attribute(self):
        wisdom = Attribute(Attribute.WISDOM, 24)
        rogue = Rogue(4)
        actor = Actor('Test Rogue With Rouge', [wisdom], [rogue])
        with self.assertRaisesRegexp(
                ValueError,
                'Dexterity is not an attribute Test Rogue With Rouge possesses.'
        ):
            actor.get_base_attribute_score(Attribute.DEXTERITY)

    def test_get_base_attribute_score_returns_requested_score(self):
        wisdom = Attribute(Attribute.WISDOM, 3)
        rogue = Rogue(13)
        actor = Actor('Test Rogue With Rouge', [wisdom], [rogue])
        self.assertEqual(actor.get_base_attribute_score(Attribute.WISDOM), 3)

    def test_get_base_attack_returns_sum_of_class_bab(self):
        fighter = Fighter(11)
        rogue = Rogue(4)
        actor = Actor('Fighter Rogue', [], [fighter, rogue])
        self.assertEqual(actor.get_base_attack_bonus().value, 14)
        self.assertEqual(
            actor.get_base_attack_bonus().audit_explanation,
            '+3 from level 4 Rogue. +11 from level 11 Fighter. '
        )

    def test_get_base_attack_returns_empty_modifier_for_classless_actor(self):
        actor = Actor('Fighter Rogue', [], [])
        self.assertEqual(actor.get_base_attack_bonus().value, 0)
        self.assertEqual(actor.get_base_attack_bonus().audit_explanation, '')
