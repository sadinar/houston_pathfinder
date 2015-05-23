__author__ = 'John Mullins'

from attribute import Attribute
from character_class import CharacterClass


class Actor(object):

    def __init__(self, name, attributes, character_classes):
        self.name = name
        self.character_classes = []
        self.base_attributes = {}
        for attribute in attributes:
            if not isinstance(attribute, Attribute):
                raise TypeError('Unable to initialize actor using unknown attribute type')
            self.base_attributes[attribute.name] = attribute
        for character_class in character_classes:
            if not isinstance(character_class, CharacterClass):
                raise TypeError('Unable to initialize actor using unknown character class')
            self.character_classes.append(character_class)

    def get_attack_bonus(self, attribute_names):
        if not isinstance(attribute_names, list):
            raise ValueError('A list of attributes, possibly empty, must be provided to calculate attack bonus')

        # Ensure there is at least a beginning attack bonus of nothing
        base_attack_bonus = 0

        # Add bonuses from all attached character classes to get total base attack
        for character_class in self.character_classes:
            base_attack_bonus += character_class.get_base_attack_bonus()

        attack_bonuses = Actor._add_additional_attacks(base_attack_bonus)

        # Once all additional attacks are found, modify bonuses by all requested attributes
        for attribute_name in attribute_names:
            for index, attack_bonus in enumerate(attack_bonuses):
                attack_bonuses[index] += self.base_attributes[attribute_name].get_attribute_modifier()

        return attack_bonuses

    @staticmethod
    def _add_additional_attacks(base_attack_bonus):
        attack_bonus = [base_attack_bonus]
        weakest_attack = attack_bonus[-1]
        if weakest_attack - 5 > 0:
            attack_bonus += (Actor._add_additional_attacks(weakest_attack - 5))

        return attack_bonus

    def get_fortitude_save(self):
        fortitude_save = 0
        if Attribute.CONSTITUTION in self.base_attributes.keys():
            fortitude_save += self.base_attributes[Attribute.CONSTITUTION].get_attribute_modifier()
        for character_class in self.character_classes:
            fortitude_save += character_class.get_fortitude_save()

        return fortitude_save

    def get_reflex_save(self):
        reflex_save = 0
        if Attribute.DEXTERITY in self.base_attributes.keys():
            reflex_save += self.base_attributes[Attribute.DEXTERITY].get_attribute_modifier()
        for character_class in self.character_classes:
            reflex_save += character_class.get_reflex_save()

        return reflex_save

    def get_will_save(self):
        will_save = 0
        if Attribute.WISDOM in self.base_attributes.keys():
            will_save += self.base_attributes[Attribute.WISDOM].get_attribute_modifier()
        for character_class in self.character_classes:
            will_save += character_class.get_will_save()

        return will_save
