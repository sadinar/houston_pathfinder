__author__ = 'John Mullins'

from saving_throw import SavingThrow
from attribute import Attribute


class Fortitude(SavingThrow):

    """Concrete implementation of fortitude save"""

    def _add_default_attribute(self):
        self.add_attribute_to_save_modifiers(Attribute.CONSTITUTION)

    def _set_name(self):
        self.name = SavingThrow.FORTITUDE
