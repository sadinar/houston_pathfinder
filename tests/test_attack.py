__author__ = 'John Mullins'

import unittest
from attack import Attack
from attribute import Attribute
from character_classes.fighter import Fighter
from character_classes.rogue import Rogue

class TestAttack(unittest.TestCase):

    def test_attack_stores_initialized_values(self):
        dexterity = Attribute(Attribute.DEXTERITY, 17)
        strength = Attribute(Attribute.STRENGTH, 13)
        fighter = Fighter(7)
        attack = Attack('some name', [strength], [dexterity], [fighter])
        self.assertEqual('some name', attack.name)
        self.assertEqual(strength, attack._damage_attributes[Attribute.STRENGTH])
        self.assertEqual(dexterity, attack._to_hit_attributes[Attribute.DEXTERITY])
        self.assertEqual(fighter, attack._character_classes[fighter.name])

    def test_attack_generates_base_attack_bonus(self):
        dexterity = Attribute(Attribute.DEXTERITY, 15)
        strength = Attribute(Attribute.STRENGTH, 9)
        fighter = Fighter(8)
        rogue = Rogue(3)

        attack = Attack('some name', [strength], [dexterity], [fighter, rogue])
        self.assertEqual(10, attack.get_base_attack_bonus().value)
        self.assertEqual(
            '+2 from level 3 Rogue. +8 from level 8 Fighter. ',
            attack.get_base_attack_bonus().audit_explanation
        )

    def test_attack_generates_full_attack(self):
        dexterity = Attribute(Attribute.DEXTERITY, 12)
        strength = Attribute(Attribute.STRENGTH, 14)
        fighter = Fighter(2)
        rogue = Rogue(13)

        attack = Attack('some name', [strength], [dexterity], [fighter, rogue])
        full_attack = attack.get_full_attacks()
        self.assertEqual(len(full_attack), 3)
        self.assertEqual(12, full_attack[0].value)
        self.assertEqual(
            '+9 from level 13 Rogue. +2 from level 2 Fighter. +1, Dexterity ability score of 12. ',
            full_attack[0].audit_explanation
        )
        self.assertEqual(7, full_attack[1].value)
        self.assertEqual(
            'Additional attack split from base BAB at a +5 breakpoint. See first attack for full audit trail.',
            full_attack[1].audit_explanation
        )
        self.assertEqual(2, full_attack[2].value)
        self.assertEqual(
            'Additional attack split from base BAB at a +5 breakpoint. See first attack for full audit trail.',
            full_attack[2].audit_explanation
        )
