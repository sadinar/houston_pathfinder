__author__ = 'John Mullins'

class Attribute:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_attribute_modifier(self):
        reduced_score = self.score - 10
        if reduced_score > 35:
            reduced_score = 35
        return reduced_score / 2
