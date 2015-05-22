__author__ = 'John Mullins'

class Attribute:

    STRENGTH = 'Strength'
    CONSTITUTION = 'Constitution'
    ABILITY_SCORE_NAMES = [
        STRENGTH,
        CONSTITUTION
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
        return (self.score - 10) / 2
