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
    self.assertEqual(['credit', 'products', 'states'], self.genericRules.categories)

  def testRulesImportCreationCustom(self):
    """
    test if RulesImport object was instantiated properly using custom params
    """
    self.customRules = RulesImport('CSV', ['credit'])
    self.assertTrue(isinstance(self.customRules, Rules))

    self.assertEqual('CSV', self.customRules.source)
    self.assertEqual(['credit'], self.customRules.categories)
