__author__ = 'John Mullins'

from modifier import Modifier


class Attack(object):

    """Represents a single attack and tracks the attributes and modifiers which impact the attack as well as
    calculating the attack and damage associated with the attack.

    Attributes:
        name (string): The attack's name
        damage_attributes (dict[Attribute]): Dictionary of attributes which enhance the attack's damage
        to_hit_attributes (dict[Attribute]): Dictionary of attributes which improve the chance to hit
        character_classes (dict[CharacterClass]): Dictionary of character classes whose base attack bonuses comprise
            the basis of the attack's chance to hit and dictate the number of initial additional attacks
    """

    def __init__(self, name, damage_attributes, to_hit_attributes, character_classes):
        """Creates an attack instance which uses the provided attributes and classes to calculate attack values.

        Args:
            name (string): Name of the attack
            damage_attributes (list[Attribute]): List of attributes which modify the damage reported by the attack
            to_hit_attributes (list[Attribute]): List of attributes used to modify attack's chance to hit
            character_classes (list[CharacterClass]): List of character classes used to generate basis for attack
        """
        self.name = name
        self._damage_attributes = {}
        for damage_attribute in damage_attributes:
            self._damage_attributes[damage_attribute.name] = damage_attribute
        self._to_hit_attributes = {}
        for to_hit_attribute in to_hit_attributes:
            self._to_hit_attributes[to_hit_attribute.name] = to_hit_attribute
        self._character_classes = {}
        for character_class in character_classes:
            self._character_classes[character_class.name] = character_class

    def _add_additional_attacks(self, base_attack_modifier):
        """Given a base attack bonus(BAB), adds additional attacks derived strictly from sufficiently high BAB bonus.

        Args:
            base_attack_bonus (Modifier): BAB with no additional attacks included

        Returns:
            list of Modifiers representing attack bonus for each BAB-based available attack
        """
        attack_bonus = [base_attack_modifier]
        weakest_attack = attack_bonus[-1]
        if weakest_attack.value - 5 > 0:
            attack_bonus += self._add_additional_attacks(
                Modifier(
                    weakest_attack.value - 5,
                    'Additional attack split from base BAB at a +5 breakpoint. See first attack for full audit trail.'
                )
            )
        return attack_bonus

    def get_base_attack_bonus(self):
        """Adds bonuses from all attached character classes to get total base attack

        Args:
            character_classes (list[CharacterClass]): List of all character classes whose BABs will be combined

        Returns:
            Modifier containing total BAB along with audit trail showing each class' contribution
        """
        base_attack_modifier = Modifier(0, '')
        for character_class in self._character_classes.values():
            # sum the BAB bonuses of each class
            class_base_bonus = character_class.get_base_attack_bonus()
            base_attack_modifier.value += class_base_bonus
            base_attack_modifier.audit_explanation += '{:+d}'.format(class_base_bonus) + ' from level '\
                + str(character_class.level) + ' ' + character_class.name + '. '
        return base_attack_modifier

    def get_full_attacks(self):
        """Calculates attack modifiers for each attack derived from a BAB using class and attribute bonuses.

        Args:
            attributes (list[Attribute]): Attributes whose bonuses will be applied to the attacks
            character_classes (list[CharacterClass]): Character classes whose BABs will be combined to create a single
                base BAB

        Returns:
            List of Modifiers describing the bonus for each attack. See the first attack for the full audit trail
            of the bonuses.
        """
        split_attacks = self._add_additional_attacks(self.get_base_attack_bonus())
        for index, attack in enumerate(split_attacks):
            # add specified attribute bonus to attacks
            for attribute in self._to_hit_attributes.values():
                attribute_modifier = attribute.get_attribute_modifier()
                attack.value += attribute_modifier.value
                if index == 0:
                    # add audit trail only to first entry
                    attack.audit_explanation += attribute_modifier.audit_explanation
        return split_attacks

    def get_damage(self):
        """Calculates attack damage"""
        # Calculate total modifier
        damage_modifier = Modifier(0, '')
        for attribute in self._damage_attributes.values():
            attribute_modifier = attribute.get_attribute_modifier()
            damage_modifier.value += attribute_modifier.value
            damage_modifier.audit_explanation += attribute_modifier.audit_explanation

        # Add to the weapon damage
        # Create a damage class?

        return '1d3+' + str(damage_modifier.value)
