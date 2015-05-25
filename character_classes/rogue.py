__author__ = 'John Mullins'

from character_class import CharacterClass


class Rogue(CharacterClass):

    """Concrete implementation of the Rogue character class"""

    @property
    def name(self):
        return 'Rogue'

    def get_base_attack_bonus(self):
        return self._get_medium_progression_attack_bonus(self.level)

    def get_fortitude_save(self):
        return self._get_saving_throw_modifier(self._get_slow_progression_save(self.level))

    def get_reflex_save(self):
        return self._get_saving_throw_modifier(self._get_fast_progression_save(self.level))

    def get_will_save(self):
        return self._get_saving_throw_modifier(self._get_slow_progression_save(self.level))
