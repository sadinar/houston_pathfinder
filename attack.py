__author__ = 'John Mullins'

from abc import ABCMeta
from modifier import Modifier


class Attack(object):

    __metaclass__ = ABCMeta

    @staticmethod
    def add_additional_attacks(base_attack_modifier):
        """Given a base attack bonus(BAB), adds additional attacks derived strictly from sufficiently high BAB bonus.

        Args:
            base_attack_bonus (Modifier): BAB with no additional attacks included

        Returns:
            list of Modifiers representing attack bonus for each BAB-based available attack
        """
        attack_bonus = [base_attack_modifier]
        weakest_attack = attack_bonus[-1]
        if weakest_attack.value - 5 > 0:
            attack_bonus += Attack.add_additional_attacks(
                Modifier(
                    weakest_attack.value - 5,
                    'Additional attack split from base BAB at a +5 breakpoint. See first attack for full audit trail.'
                )
            )
        return attack_bonus

    @staticmethod
    def get_base_attack_bonus(character_classes):
        """Adds bonuses from all attached character classes to get total base attack

        Args:
            character_classes (list[CharacterClass]): List of all character classes whose BABs will be combined

        Returns:
            Modifier containing total BAB along with audit trail showing each class' contribution
        """
        base_attack_modifier = Modifier(0, '')
        for character_class in character_classes:
            # sum the BAB bonuses of each class
            class_base_bonus = character_class.get_base_attack_bonus()
            base_attack_modifier.value += class_base_bonus
            base_attack_modifier.audit_explanation += '{:+d}'.format(class_base_bonus) + ' from level '\
                + str(character_class.level) + ' ' + character_class.name + '. '
        return base_attack_modifier

    @staticmethod
    def get_full_attacks(attributes, character_classes):
        """Calculates attack modifiers for each attack derived from a BAB using class and attribute bonuses.

        Args:
            attributes (list[Attribute]): Attributes whose bonuses will be applied to the attacks
            character_classes (list[CharacterClass]): Character classes whose BABs will be combined to create a single
                base BAB

        Returns:
            List of Modifiers describing the bonus for each attack. See the first attack for the full audit trail
            of the bonuses.
        """
        split_attacks = Attack.add_additional_attacks(Attack.get_base_attack_bonus(character_classes))
        for index, attack in enumerate(split_attacks):
            # add specified attribute bonus to attacks
            for attribute in attributes:
                attribute_modifier = attribute.get_attribute_modifier()
                attack.value += attribute_modifier.value
                if index == 0:
                    # add audit trail only to first entry
                    attack.audit_explanation += attribute_modifier.audit_explanation
        return split_attacks
