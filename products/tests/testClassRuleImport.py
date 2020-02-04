from django.test import TestCase

from ..classes.rulesImport import RulesImport
from ..classes.rule import *

class ProductsClassRulesImportTest(TestCase):

  def setUp(self):
    self.genericCategories = RulesImport()

  def testRulesImportCreationDefault(self):
    """
    test if RulesImport object was instantiated properly using default params
    """
    self.assertTrue(isinstance(self.genericCategories, RulesImport))

    self.assertEqual('JSON', self.genericCategories.source)
    self.assertEqual(['credit', 'products', 'states'], self.genericCategories.categories)

  def testRulesImportCreationCustom(self):
    """
    test if RulesImport object was instantiated properly using custom params
    """
    self.customRules = RulesImport('CSV', ['credit'])
    self.assertTrue(isinstance(self.customRules, RulesImport))

    self.assertEqual('CSV', self.customRules.source)
    self.assertEqual(['credit'], self.customRules.categories)

  def testRulesImportCreditCreation(self):
    """
    test if RulesImport object was instantiated properly using Credit Rule
    """
    rule = RulesImport('JSON', ['credit'])
    self.assertTrue(isinstance(rule.rules[0], CreditRule))

  def testRulesImportDebtCreation(self):
    """
    test if RulesImport object was instantiated properly using Debt Rule
    """
    rule = RulesImport('JSON', ['debt'])
    self.assertTrue(isinstance(rule.rules[0], DebtRule))

  def testRulesImportEmploymentCreation(self):
    """
    test if RulesImport object was instantiated properly using Employment Rule
    """
    rule = RulesImport('JSON', ['employment'])
    self.assertTrue(isinstance(rule.rules[0], EmploymentRule))

  def testRulesImportIncomeCreation(self):
    """
    test if RulesImport object was instantiated properly using Income Rule
    """
    rule = RulesImport('JSON', ['income'])
    self.assertTrue(isinstance(rule.rules[0], IncomeRule))

  def testRulesImportProductsCreation(self):
    """
    test if RulesImport object was instantiated properly using Products Rule
    """
    rule = RulesImport('JSON', ['products'])
    self.assertTrue(isinstance(rule.rules[0], ProductsRule))

  def testRulesImportStatesCreation(self):
    """
    test if RulesImport object was instantiated properly using States Rule
    """
    rule = RulesImport('JSON', ['states'])
    self.assertTrue(isinstance(rule.rules[0], StatesRule))