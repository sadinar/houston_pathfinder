__author__ = 'John Mullins'


class Modifier(object):

    """Provides a means to explain where a modifier came from and treat it as a basic type when appropriate.

    Attributes:
        value (int): The modifier (possibly a bonus, penalty, or zero) used for both calculation and display purposes
        audit_explanation (string): Explanation of where the modifier originated and may contain other modifiers'
            audit explanations
        dice_type (int): Type of die added by the modifier (d6 would be 6, d8 would be 8, etc.)
        dice_count (int): Number of dice added by the modifier (2d6 would be 2, 1d6 would be 1, etc.)
    """

    def __init__(self, value, audit_explanation=''):
        self.value = value
        self.audit_explanation = audit_explanation
