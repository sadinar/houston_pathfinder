__author__ = 'John Mullins'

from attribute import Attribute
from character_class import CharacterClass


class Actor(object):

    """Represents the sum total of a being who can be a player character, monster, or NPC, in the game world. Provides
    attacks, defenses, saving throws, equipment, feats, race, background, and more. Utility methods retrieve modifiers
    and descriptions as well as an audit trail to explain how modifiers were calculated.

    Attributes:
        name (string): Actor's name
        character_classes (list[CharacterClass): List of all character classes the Actor has at least one level in
        base_attributes (dict[Attribute]): Dictionary of Attributes indexed by attribute name detailing the
            character's permanent attributes. Permanent attributes include those assigned during creation and through
            addition of character classes, but do not include temporary modifiers
    """

    def __init__(self, name, attributes, character_classes):
        """Creates and actor using provided information

        Args:
            name (string): Name of the character used for display purposes only
            attributes (list[Attribute]): List of Attribute objects assigned to the character
            character_classes (list[CharacterClass]): List of CharacterClass objects representing the levels and
                decisions made for character's classes
        """
        self.name = name
        self.character_classes = []
        self.base_attributes = {}

        for attribute in attributes:
            if not isinstance(attribute, Attribute):
                raise TypeError('Unable to initialize actor using unknown attribute type')
            self.base_attributes[attribute.name] = attribute
        for character_class in character_classes:
            if not isinstance(character_class, CharacterClass):
                raise TypeError('Unable to initialize actor using unknown character class')
            self.character_classes.append(character_class)

    def get_attack_bonus(self, attribute_names):
        """Returns attack bonus, including temporary modifiers, permanent modifiers, and additional attacks. Capable
        of combining bonuses across multiple classes and attributes.

        Args:
            attribute_names (list[string]): List of attributes whose modifiers should be added to the attack
                calculation. Names must be from the list of valid attribute names found in Attribute

        Returns:
            list if ints representing attack bonus for each available attack
        """
        if not isinstance(attribute_names, list):
            raise ValueError('A list of attributes, possibly empty, must be provided to calculate attack bonus')

        # Ensure there is at least a beginning attack bonus of nothing
        base_attack_bonus = 0

        # Add bonuses from all attached character classes to get total base attack
        for character_class in self.character_classes:
            base_attack_bonus += character_class.get_base_attack_bonus()

        attack_bonuses = Actor._add_additional_attacks(base_attack_bonus)

        # Once all additional attacks are found, modify bonuses by all requested attributes
        for attribute_name in attribute_names:
            for index, attack_bonus in enumerate(attack_bonuses):
                attack_bonuses[index] += self.base_attributes[attribute_name].get_attribute_modifier().value

        return attack_bonuses

    @staticmethod
    def _add_additional_attacks(base_attack_bonus):
        """Given a base attack bonus(BAB), adds additional attacks derived strictly from sufficiently high BAB bonus.

        Args:
            base_attack_bonus (int): BAB with no additional attacks included

        Returns:
            list of ints representing base attack bonus for each available attack
        """
        attack_bonus = [base_attack_bonus]
        weakest_attack = attack_bonus[-1]
        if weakest_attack - 5 > 0:
            attack_bonus += (Actor._add_additional_attacks(weakest_attack - 5))

        return attack_bonus

    def get_fortitude_save(self):
        """ Returns character's fortitude saving throw by combining attribute bonus with bonuses across classes

        Returns:
            int representing fortitude saving throw
        """
        fortitude_save = 0
        if Attribute.CONSTITUTION in self.base_attributes.keys():
            fortitude_save += self.base_attributes[Attribute.CONSTITUTION].get_attribute_modifier().value
        for character_class in self.character_classes:
            fortitude_save += character_class.get_fortitude_save()

        return fortitude_save

    def get_reflex_save(self):
        """ Returns character's reflex saving throw by combining attribute bonus with bonuses across classes

        Returns:
            int representing reflex saving throw
        """
        reflex_save = 0
        if Attribute.DEXTERITY in self.base_attributes.keys():
            reflex_save += self.base_attributes[Attribute.DEXTERITY].get_attribute_modifier().value
        for character_class in self.character_classes:
            reflex_save += character_class.get_reflex_save()

        return reflex_save

    def get_will_save(self):
        """ Returns character's will saving throw by combining attribute bonus with bonuses across classes

        Returns:
            int representing will saving throw
        """
        will_save = 0
        if Attribute.WISDOM in self.base_attributes.keys():
            will_save += self.base_attributes[Attribute.WISDOM].get_attribute_modifier().value
        for character_class in self.character_classes:
            will_save += character_class.get_will_save()

        return will_save
