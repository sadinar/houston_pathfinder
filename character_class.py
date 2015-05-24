__author__ = 'John Mullins'

from abc import ABCMeta, abstractmethod
from saving_throw import SavingThrow


class CharacterClass(object):

    """Abstract class which provides the basic framework and behavior of all concrete character class implementations.

    Attributes:
        level (int): Character's current level in a specific class instance
        name (string): Name of the concrete class being modeled
    """

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

    def get_saving_throw(self, name):
        """Returns specified saving throw."""
        if name not in SavingThrow.SAVING_THROW_NAMES:
            raise ValueError(name + ' is not a valid saving throw name')
        if name == SavingThrow.FORTITUDE:
            return self.get_fortitude_save()
        if name == SavingThrow.REFLEX:
            return self.get_reflex_save()
        if name == SavingThrow.WILL:
            return self.get_will_save()

    @abstractmethod
    def get_base_attack_bonus(self):
        """Calculates base attack bonus for the class using its level. Does not include extra attacks or modifiers"""
        pass

    @abstractmethod
    def get_fortitude_save(self):
        """Calculates fortitude saving throw for the class using its level. Does not include modifiers"""
        pass

    @abstractmethod
    def get_reflex_save(self):
        """Calculates reflex saving throw for the class using its level. Does not include modifiers"""
        pass

    @abstractmethod
    def get_will_save(self):
        """Calculates will saving throw for the class using its level. Does not include modifiers"""
        pass

    @staticmethod
    def _get_fast_progression_attack_bonus(level):
        """Calculates base attack bonus (BAB) for fast attacks and should not be called directly.
        Use a concrete class' get_base_attack_bonus implementation instead to get the BAB for a specific class

        Args:
            level (int): Integer denoting character's current level in the class

        Returns:
            An integer representing BAB of a fast progression class, such as a Fighter, at the specified level.
            Does not include additional attacks
        """
        return level

    @staticmethod
    def _get_medium_progression_attack_bonus(level):
        """Calculates base attack bonus (BAB) for medium attacks and should not be called directly.
        Use a concrete class' get_base_attack_bonus implementation instead to get the BAB for a specific class

        Args:
            level (int): Integer denoting character's current level in the class

        Returns:
            An integer representing BAB of a medium progression class, such as a Rogue, at the specified level.
            Does not include additional attacks
        """
        return level * 3 / 4

    @staticmethod
    def _get_slow_progression_attack_bonus(level):
        """Calculates base attack bonus (BAB) for slow attacks and should not be called directly.
        Use a concrete class' get_base_attack_bonus implementation instead to get the BAB for a specific class

        Args:
            level (int): Integer denoting character's current level in the class

        Returns:
            An integer representing BAB of a slow progression class, such as a Wizard, at the specified level.
            Does not include additional attacks
        """
        return level / 2

    @staticmethod
    def _get_fast_progression_save(level):
        """Calculates fast progression saving throw (save) and should not be called directly. Use a concrete class'
         get_fortitude_save, get_reflex_save, or get_will_save implementation instead to get a specific save

        Args:
            level (int): Integer denoting character's current level in the class

        Returns:
            An integer representing save of a fast progression class, such as a Monk, at the specified level.
        """
        return 2 + level / 2

    @staticmethod
    def _get_slow_progression_save(level):
        """Calculates slow progression saving throw (save) and should not be called directly. Use a concrete class'
         get_fortitude_save, get_reflex_save, or get_will_save implementation instead to get a specific save

        Args:
            level (int): Integer denoting character's current level in the class

        Returns:
            An integer representing save of a slow progression class, such as Fighter's will save, at specified level.
        """
        return level / 3
