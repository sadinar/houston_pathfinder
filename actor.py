__author__ = 'John Mullins'

from character_classes.fighter import Fighter

class Actor:
    def __init__(self, name, attributes):
        self.name = name
        self.character_class = Fighter(13)
        self.base_attributes = {}
        for attribute in attributes:
            self.base_attributes[attribute.name] = attribute

    def get_attack_bonus(self, attribute_names):
        attribute_bonus = 0
        for attribute_name in attribute_names:
            attribute_bonus += self.base_attributes[attribute_name].get_attribute_modifier()
        return attribute_bonus + self.character_class.get_base_attack_bonus()

    def get_fortitude_save(self):
        return self.character_class.get_fortitude_save()

    def get_reflex_save(self):
        return self.character_class.get_reflex_save()

    def get_will_save(self):
        return self.character_class.get_will_save()

# tahlen = Actor('Tahlen')
# print tahlen.name + '\'s strength is {0:d}'.format(tahlen.base_attributes['Strength'].score)
# print tahlen.name + '\'s attack bonus is +{0:d}'.format(tahlen.get_attack_bonus(['Strength']))
# print tahlen.name + '\'s fort save is {0:d}'.format(tahlen.get_fortitude_save())
# print tahlen.name + '\'s reflex save is {0:d}'.format(tahlen.get_reflex_save())
# print tahlen.name + '\'s will save is {0:d}'.format(tahlen.get_will_save())
