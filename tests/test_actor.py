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
        actor = Actor('Blank guy', [], [])
        self.assertEqual(actor.get_base_attack_bonus().value, 0)
        self.assertEqual(actor.get_base_attack_bonus().audit_explanation, '')

    def test_get_full_attack_returns_list_of_modifiers(self):
        fighter = Fighter(2)
        rogue = Rogue(19)
        actor = Actor('Rogue Fighter', [], [rogue, fighter])
        full_attack = actor.get_full_attack([])
        self.assertEqual(len(full_attack), 4)
        self.assertEqual(full_attack[0].value, 16)
        self.assertEqual(full_attack[0].audit_explanation, '+14 from level 19 Rogue. +2 from level 2 Fighter. ')
        self.assertEqual(full_attack[1].value, 11)
        self.assertEqual(
            full_attack[1].audit_explanation,
            'Additional attack split from base BAB at a +5 breakpoint. See first attack for full audit trail.'
        )
        self.assertEqual(full_attack[2].value, 6)
        self.assertEqual(
            full_attack[2].audit_explanation,
            'Additional attack split from base BAB at a +5 breakpoint. See first attack for full audit trail.'
        )
        self.assertEqual(full_attack[3].value, 1)
        self.assertEqual(
            full_attack[3].audit_explanation,
            'Additional attack split from base BAB at a +5 breakpoint. See first attack for full audit trail.'
        )

    def test_get_full_attack_adds_requested_attributes(self):

        fighter = Fighter(5)
        rogue = Rogue(16)
        strength = Attribute(Attribute.STRENGTH, 16)
        dexterity = Attribute(Attribute.DEXTERITY, 14)
        actor = Actor('Rogue Fighter', [strength, dexterity], [rogue, fighter])
        full_attack = actor.get_full_attack([strength.name, dexterity.name])
        self.assertEqual(len(full_attack), 4)
        self.assertEqual(full_attack[0].value, 22)
        self.assertEqual(
            full_attack[0].audit_explanation,
            '+12 from level 16 Rogue. +5 from level 5 Fighter. +3, Strength ability score of 16. +2, ' +
            'Dexterity ability score of 14. '
        )
        self.assertEqual(full_attack[1].value, 17)
        self.assertEqual(
            full_attack[1].audit_explanation,
            'Additional attack split from base BAB at a +5 breakpoint. See first attack for full audit trail.'
        )
        self.assertEqual(full_attack[2].value, 12)
        self.assertEqual(
            full_attack[2].audit_explanation,
            'Additional attack split from base BAB at a +5 breakpoint. See first attack for full audit trail.'
        )
        self.assertEqual(full_attack[3].value, 7)
        self.assertEqual(
            full_attack[3].audit_explanation,
            'Additional attack split from base BAB at a +5 breakpoint. See first attack for full audit trail.'
        )
