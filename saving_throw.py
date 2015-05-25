__author__ = 'John Mullins'

from attribute import Attribute
from modifier import Modifier


class SavingThrow(object):

    """Maintains the aggregate modifier for one of an actor's saving throws. Includes class, attribute, and
    other modifiers

    Attributes:
        actor (Actor): Actor whose saving throw is being tracked
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

    def __init__(self, actor, name):
        """Creates a single saving throw for an actor

        Args:
            actor (Actor): Actor whose saving throw is being tracked
            name (string): Name of the saving throw which must be from the valid list of names
        """
        self.actor = actor
        self.applicable_attributes = []

        if name not in self.SAVING_THROW_NAMES:
            raise ValueError(name + ' is not a valid saving throw name')
        self.name = name

        # Initialize attribute bonus
        if name == self.FORTITUDE:
            self.add_attribute_to_save_modifiers(Attribute.CONSTITUTION)
        elif name == self.REFLEX:
            self.add_attribute_to_save_modifiers(Attribute.DEXTERITY)
        else:
            self.add_attribute_to_save_modifiers(Attribute.WISDOM)

        # Calculate save based on initial information
        self.modifier = self._calculate_save()

    def _calculate_save(self):
        """Calculates the modifier representing the saving throw.

        Return
            Modifier containing the save plus an audit trail
        """
        total_save = Modifier(0)
        for character_class in self.actor.character_classes:
            class_bonus = character_class.get_saving_throw(self.name)
            total_save.value += class_bonus.value
            total_save.audit_explanation += class_bonus.audit_explanation
        for attribute in self.applicable_attributes:
            attribute_bonus = self.actor.get_attribute_modifier(attribute)
            total_save.value += attribute_bonus.value
            total_save.audit_explanation += attribute_bonus.audit_explanation

        return total_save

    def add_attribute_to_save_modifiers(self, attribute_name):
        """Adds an attribute to the list of attributes whose modifiers are used when calculating the saving throw

        Args:
            attribute_name (string): Name of the attribute being added
        """
        if attribute_name not in self.applicable_attributes:
            self.applicable_attributes.append(attribute_name)
            self.modifier = self._calculate_save()
