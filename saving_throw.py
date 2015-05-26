__author__ = 'John Mullins'

from modifier import Modifier
from attribute import Attribute


class SavingThrow(object):

    """Maintains the aggregate modifier for one of an actor's saving throws. Includes class, attribute, and
    other modifiers

    Attributes:
        name (string): Name of the saving throw, chosen only from the list of valid names
        _attributes (dict[Attribute]): List of Attributes belonging to the actor whose modifiers should be
            applied to the saving throw, indexed by name
        _character_classes (list[CharacterClass]): List of CharacterClasses which apply to the saving throw
        FORTITUDE (string): Name of fortitude saving throw
        REFLEX (string): Name of reflex saving throw
        WILL (string): Name of will saving throw
        SAVING_THROW_NAMES (list[string]): list of valid saving throw names
        BASE_ATTRIBUTES (list[string[): list of attributes serving as the basis for specific saving throws
    """

    FORTITUDE = 'Fortitude'
    REFLEX = 'Reflex'
    WILL = 'Will'
    SAVING_THROW_NAMES = [FORTITUDE, REFLEX, WILL]
    BASE_ATTRIBUTES = {
        FORTITUDE: Attribute.CONSTITUTION,
        REFLEX: Attribute.DEXTERITY,
        WILL: Attribute.WISDOM
    }

    def __init__(self, name, character_classes, base_attribute):
        """Creates a single saving throw for an actor

        Args:
            name (string): Name of the saving throw
            character_classes (list[CharacterClass]): Character classes whose saves should be included
            attribute (Attribute): Base attribute for the saving throw
        """

        self.name = name
        self._character_classes = character_classes
        if base_attribute is not None:
            self._attributes = {base_attribute.name: base_attribute}
        else:
            self._attributes = {}

    def get_modifier(self):
        """Calculates the modifier representing the saving throw.

        Return
            Modifier containing the save plus an audit trail
        """
        total_save_modifier = Modifier(0)
        for character_class in self._character_classes:
            class_bonus = character_class.get_saving_throw(self.name)
            total_save_modifier.value += class_bonus.value
            total_save_modifier.audit_explanation += class_bonus.audit_explanation
        for attribute in self._attributes.values():
            attribute_modifier = attribute.get_attribute_modifier()
            total_save_modifier.value += attribute_modifier.value
            total_save_modifier.audit_explanation += attribute_modifier.audit_explanation

        return total_save_modifier

    def add_attribute(self, attribute):
        """Adds an Attribute to the list of Attributes whose modifiers are used when calculating the saving throw.
        If an Attribute with the same name already exists, will replace the existing Attribute

        Args:
            attribute_name (string): Name of the attribute being added
        """
        self._attributes[attribute.name] = attribute

    def remove_attribute(self, attribute_name):
        """Removes the specified attribute from the dictionary of attributes modifying the save"""
        if attribute_name in self._attributes.keys():
            del self._attributes[attribute_name]
