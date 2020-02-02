from django.urls import reverse
from django.test import TestCase

from ..classes.rulesImport import RulesImport
from ..classes.rules import Rules

class ProductsClassRulesImportTest(TestCase):

  def setUp(self):
    self.genericRules = RulesImport()

  def testRulesImportCreationDefault(self):
    """
    test if RulesImport object was instantiated properly using default params
    """
    self.assertTrue(isinstance(self.genericRules, Rules))

    self.assertEqual('JSON', self.genericRules.source)
    self.assertEqual(['credit', 'products', 'states'], self.genericRules.rules)

  """def testPersonMethodSetIncome(self):
    self.genericPerson.setIncome(False, 52000, 0.5)

    self.assertEqual(False, self.genericPerson.currentlyEmployed)
    self.assertEqual(52000, self.genericPerson.currentIncome)
    self.assertEqual(0.5, self.genericPerson.debtToIncome)"""
