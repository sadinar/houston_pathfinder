__author__ = 'John Mullins'


class Modifier(object):

    """Provides a means to explain where a modifier came from and treat it as a basic type when appropriate.

    Attributes:
        value (int): The modifier (possibly a bonus, penalty, or zero) used for both calculation and display purposes
        audit_explanation (string): Explanation of where the modifier originated and may contain other modifiers'
            audit explanations
    """

    def __init__(self, value, audit_explanation):
        self.value = value
        self.audit_explanation = audit_explanation
