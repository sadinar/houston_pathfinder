__author__ = 'John Mullins'

from saving_throw import SavingThrow
from attribute import Attribute


class Will(SavingThrow):

    """Concrete implementation of will save"""

    def _add_default_attribute(self):
        self.add_attribute_to_save_modifiers(Attribute.WISDOM)

    def _set_name(self):
        self.name = SavingThrow.WILL
