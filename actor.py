__author__ = 'John Mullins'

from attribute import Attribute
from character_class import CharacterClass
from saving_throw import SavingThrow
from modifier import Modifier
from attack import Attack


class Actor(object):

    """Represents the sum total of a being who can be a player character, monster, or NPC, in the game world. Provides
    attacks, defenses, saving throws, equipment, feats, race, background, and more. Utility methods retrieve modifiers
    and descriptions as well as an audit trail to explain how modifiers were calculated.

    Attributes:
        name (string): Actor's name
        _character_classes (dict[CharacterClass): Dict of all character classes the Actor has at least one level in
        _attributes (dict[Attribute]): Dictionary of Attributes indexed by attribute name detailing the
            character's permanent attributes. Permanent attributes include those assigned during creation and through
            addition of character classes, but do not include temporary modifiers
        _saving_throws (dict[SavingThrow]): Provides the actor's saves, including temporary and permanent modifiers,
            along with audit trail. Dictionary is indexed by save name from the SavingThrow class
    """

    def __init__(self, name, attributes, character_classes):
        """Creates and actor using provided information

        Args:
            name (string): Name of the character used for display purposes only
            attributes (list[Attribute]): List of Attribute objects assigned to the character. Does not include
                temporary modifiers of any kind
            character_classes (list[CharacterClass]): List of CharacterClass objects representing the levels and
                decisions made for character's classes
        """
        self.name = name
        self._character_classes = {}
        self._attributes = {}

        for attribute in attributes:
            if not isinstance(attribute, Attribute):
                raise TypeError('Unable to initialize actor using unknown attribute type')
            self._attributes[attribute.name] = attribute
        for character_class in character_classes:
            if not isinstance(character_class, CharacterClass):
                raise TypeError('Unable to initialize actor using unknown character class')
            self._character_classes[character_class.name] = character_class

        # Initialize saving throws after classes and attributes have been assigned for complete bonuses
        self._saving_throws = {
            SavingThrow.FORTITUDE: self._initialize_saving_throw(SavingThrow.FORTITUDE),
            SavingThrow.REFLEX: self._initialize_saving_throw(SavingThrow.REFLEX),
            SavingThrow.WILL: self._initialize_saving_throw(SavingThrow.WILL),
        }

    def get_fortitude_save(self):
        """Returns the actor's fortitude saving throw including all temporary modifiers

        Return:
            Modifier object containing the saving throw along with audit trail
        """
        return self._saving_throws[SavingThrow.FORTITUDE].get_modifier()

    def get_reflex_save(self):
        """Returns the actor's reflex saving throw including all temporary modifiers

        Return:
            Modifier object containing the saving throw along with audit trail
        """
        return self._saving_throws[SavingThrow.REFLEX].get_modifier()

    def get_will_save(self):
        """Returns the actor's will saving throw including all temporary modifiers

        Return:
            Modifier object containing the saving throw along with audit trail
        """
        return self._saving_throws[SavingThrow.WILL].get_modifier()

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

    def _initialize_saving_throw(self, saving_throw_name):
        """
        Args:
            saving_throw_name (string): Name of the save being set to default values

        Returns:
            SavingThrow which uses actor's character classes and save default attribute, if available
        """
        if SavingThrow.BASE_ATTRIBUTES[saving_throw_name] in self._attributes.keys():
            save_attribute = self._attributes[SavingThrow.BASE_ATTRIBUTES[saving_throw_name]]
        else:
            save_attribute = None

        return SavingThrow(saving_throw_name, self._character_classes, save_attribute)

    def get_base_attack_bonus(self):
        """Adds bonuses from all attached character classes to get total base attack"""
        return Attack.get_base_attack_bonus(self._character_classes.values())

    def get_full_attack(self, attribute_names):
        """Creates a list of attack modifiers using BAB to calculate multiple attacks then adding additional modifiers
        to each attack.

        Args:
            attribute_names (list[string]): List of attributes from the internal _attributes dict whose bonuses
                will be added to the attack

        Returns:
            list of Modifiers representing the modifier for each attack. See the first attack in the list for the
            full audit trail
        """
        included_attributes = []
        for attribute_name in attribute_names:
            included_attributes.append(self._attributes[attribute_name])
        return Attack.get_full_attacks(included_attributes, self._character_classes.values())
