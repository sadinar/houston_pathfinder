__author__ = 'John Mullins'

from attribute import Attribute
from character_class import CharacterClass
from saving_throw import SavingThrow
from saving_throws.fortitude import Fortitude
from saving_throws.reflex import Reflex
from saving_throws.will import Will
from modifier import Modifier


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
        test_saving_throws (dict[SavingThrow]): Provides the actor's saves, including temporary and permanent modifiers,
            along with audit trail. Dictionary is indexed by save name from the SavingThrow class
    """

    def __init__(self, name, attributes, character_classes):
        """Creates and actor using provided information

        Args:
            name (string): Name of the character used for display purposes only
            base_attributes (list[Attribute]): List of Attribute objects assigned to the character. Does not include
                temporary modifiers of any kind
            character_classes (list[CharacterClass]): List of CharacterClass objects representing the levels and
                decisions made for character's classes
        """
        self.name = name
        self.character_classes = []
        self._attributes = {}

        for attribute in attributes:
            if not isinstance(attribute, Attribute):
                raise TypeError('Unable to initialize actor using unknown attribute type')
            self._attributes[attribute.name] = attribute
        for character_class in character_classes:
            if not isinstance(character_class, CharacterClass):
                raise TypeError('Unable to initialize actor using unknown character class')
            self.character_classes.append(character_class)

        # Initialize saving throws after classes and attributes have been assigned for complete bonuses
        self._saving_throws = {
            SavingThrow.FORTITUDE: Fortitude(self),
            SavingThrow.REFLEX: Reflex(self),
            SavingThrow.WILL: Will(self)
        }

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
                attack_bonuses[index] += self._attributes[attribute_name].get_attribute_modifier().value

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
        """Returns the actor's fortitude saving throw including all temporary modifiers

        Return:
            Modifier object containing the saving throw along with audit trail
        """
        return self._saving_throws[SavingThrow.FORTITUDE].modifier

    def get_reflex_save(self):
        """Returns the actor's reflex saving throw including all temporary modifiers

        Return:
            Modifier object containing the saving throw along with audit trail
        """
        return self._saving_throws[SavingThrow.REFLEX].modifier

    def get_will_save(self):
        """Returns the actor's will saving throw including all temporary modifiers

        Return:
            Modifier object containing the saving throw along with audit trail
        """
        return self._saving_throws[SavingThrow.WILL].modifier

    def get_attribute_modifier(self, attribute_name):
        """Returns modifier for specified attribute including all temporary and permanent modifiers

        Args:
            attribute_name (string): Name of the attribute whose modifier will be returned

        Returns:
            Modifier object representing total modifier along with full audit trail
        """
        if attribute_name in self._attributes:
            return self._attributes[attribute_name].get_attribute_modifier()
        return Modifier(0, self.name + ' does not have the ' + attribute_name + ' attribute.')

    def get_base_attribute_score(self, attribute_name):
        """Returns the permanent score of an attribute ignoring temporary modifiers

        Args:
            name (string): Name of the attribute whose score is being requested

        Returns:
            Int representing the raw ability score
        """
        if attribute_name not in self._attributes:
            raise ValueError(attribute_name + ' is not an attribute ' + self.name + ' possesses.')
        return self._attributes[attribute_name].score
