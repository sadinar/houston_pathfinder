__author__ = 'John Mullins'

from abc import ABCMeta, abstractmethod


class CharacterClass(object):

    __metaclass__ = ABCMeta

    def __init__(self, level=1):
        level = int(level)
        if level < 1 or level > 20:
            raise ValueError('Character levels must be numbers from 1 to 20')
        self.level = level

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def get_base_attack_bonus(self):
        pass

    @abstractmethod
    def get_fortitude_save(self):
        pass

    @abstractmethod
    def get_reflex_save(self):
        pass

    @abstractmethod
    def get_will_save(self):
        pass

    @staticmethod
    def _get_fast_progression_attack_bonus(level):
        return level

    @staticmethod
    def _get_medium_progression_attack_bonus(level):
        return level * 3 / 4

    @staticmethod
    def _get_slow_progression_attack_bonus(level):
        return level / 2

    @staticmethod
    def _get_fast_progression_save(level):
        return 2 + level / 2

    @staticmethod
    def _get_slow_progression_save(level):
        return level / 3
