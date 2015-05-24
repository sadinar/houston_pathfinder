__author__ = 'John Mullins'

from modifier import Modifier


class Attribute(object):

    """Tracks scores and derived bonuses of character attributes

    Attributes:
        name (string): Name of the attribute being tracked which must be from the list of valid names
        score (int): Value assigned to the attribute
        STRENGTH (string): Name used when tracking the strength attribute. Any other name is not recognized
        CONSTITUTION (string): Name used when tracking the constitution attribute. Any other name is not recognized
        DEXTERITY (string): Name used when tracking the dexterity attribute. Any other name is not recognized
        WISDOM (string): Name used when tracking the wisdom attribute. Any other name is not recognized
        ABILITY_SCORE_NAMES (list[string]): List of all valid ability score names
    """

    STRENGTH = 'Strength'
    CONSTITUTION = 'Constitution'
    DEXTERITY = 'Dexterity'
    WISDOM = 'Wisdom'
    ABILITY_SCORE_NAMES = [
        STRENGTH,
        CONSTITUTION,
        DEXTERITY,
        WISDOM
    ]

    def __init__(self, name, score):
        if name not in self.ABILITY_SCORE_NAMES:
            raise ValueError(name + ' is not a recognized ability score')
        self.name = name
        self.score = score
        if self.score < 1:
            self.score = 1
        elif self.score > 45:
            self.score = 45

    def get_attribute_modifier(self):
        """Returns modifier, a bonus, penalty, or zero, of the ability score"""
        modifier_value = (self.score - 10) / 2
        return Modifier(
            modifier_value,
            '{:+d}'.format(modifier_value) + ', ' + self.name + ' ability score of ' + str(self.score)
        )
