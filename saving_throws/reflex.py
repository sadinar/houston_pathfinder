__author__ = 'John Mullins'

from saving_throw import SavingThrow
from attribute import Attribute


class Reflex(SavingThrow):

    """Concrete implementation of reflex save"""

    def _add_default_attribute(self):
        self.add_attribute_to_save_modifiers(Attribute.DEXTERITY)

    def _set_name(self):
        self.name = SavingThrow.REFLEX
