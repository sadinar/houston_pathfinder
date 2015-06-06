__author__ = 'John Mullins'

import unittest
from modifier import Modifier


class TestModifier(unittest.TestCase):

    def test_modifier_has_value(self):
        modifier = Modifier(12, 'description text')
        self.assertEqual(12, modifier.value)

    def test_modifier_contains_audit_explanation(self):
        modifier = Modifier(3, 'Class skill bonus')
        self.assertEqual('Class skill bonus', modifier.audit_explanation)
