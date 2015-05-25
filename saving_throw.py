__author__ = 'John Mullins'

from modifier import Modifier
from attribute import Attribute


class SavingThrow(object):

    """Maintains the aggregate modifier for one of an actor's saving throws. Includes class, attribute, and
    other modifiers

    Attributes:
        name (string): Name of the saving throw, chosen only from the list of valid names
        modifier (Modifier): Saving throw score with all attributes, class bonuses, and miscellaneous modifiers
            as well as an audit trail
        applicable_attributes (list[string]): List of attributes belonging to the actor whose modifiers should be
            applied to the saving throw
        FORTITUDE (string): Name of fortitude saving throw
        REFLEX (string): Name of reflex saving throw
        WILL (string): Name of will saving throw
        SAVING_THROW_NAMES (list[string]): list of valid saving throw names
    """

    FORTITUDE = 'Fortitude'
    REFLEX = 'Reflex'
    WILL = 'Will'
    SAVING_THROW_NAMES = [FORTITUDE, REFLEX, WILL]

    def __init__(self, name):
        """Creates a single saving throw for an actor

        Args:
            name (string): Name of the saving throw, chosen from the list of valid names within this class
        """
        if name == self.FORTITUDE:
            self.applicable_attributes = [Attribute.CONSTITUTION]
        elif name == self.REFLEX:
            self.applicable_attributes = [Attribute.DEXTERITY]
        elif name == self.WILL:
            self.applicable_attributes = [Attribute.WISDOM]
        else:
            raise ValueError(name + ' is not a valid saving throw name')
        self.name = name
        self.modifier = None

    def calculate_save(self, character_classes, attribute_modifiers):
        """Calculates the modifier representing the saving throw.

        Args:
            character_classes (list[CharacterClass]): List of character classes whose bonuses will be applied
            attribute_modifiers (dict[string: Modifier]): Dictionary of attribute modifiers keyed by attribute name

        Return
            Modifier containing the save plus an audit trail
        """
        total_save_modifier = Modifier(0)
        for character_class in character_classes:
            class_bonus = character_class.get_saving_throw(self.name)
            total_save_modifier.value += class_bonus.value
            total_save_modifier.audit_explanation += class_bonus.audit_explanation
        for attribute in self.applicable_attributes:
            if attribute in attribute_modifiers:
                attribute_modifier = attribute_modifiers[attribute]
                total_save_modifier.value += attribute_modifier.value
                total_save_modifier.audit_explanation += attribute_modifier.audit_explanation

        self.modifier = total_save_modifier

    def add_attribute_to_save_modifiers(self, attribute_name):
        """Adds an attribute to the list of attributes whose modifiers are used when calculating the saving throw

        Args:
            attribute_name (string): Name of the attribute being added
        """
        if attribute_name not in self.applicable_attributes:
            self.applicable_attributes.append(attribute_name)
