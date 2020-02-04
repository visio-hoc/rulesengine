from django.test import TestCase

from ..classes.person import Person
from ..classes.product import Product
from ..classes.rulesImport import RulesImport
from ..classes.rulesEngine import RulesEngine

class ProductsClassRulesEngineTest(TestCase):

  def setUp(self):
    self.genericProduct = Product('TEMP', 5.0)
    self.rules_engine = RulesEngine()

  def testRulesImportGoodCreditCheck(self):
    """
    test good credit against RulesEngine
    """
    person = Person(800, 'NEVERLAND')

    rules = RulesImport('JSON', ['credit'])
    goodPoints = rules.rules[0].data['GOOD']['basis_points']
    newRate = self.genericProduct.interest_rate - goodPoints

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(newRate, self.rules_engine.product.interest_rate)

  def testRulesImportBadCreditCheck(self):
    """
    test bad credit against RulesEngine
    """
    person = Person(500, 'NEVERLAND')
    
    rules = RulesImport('JSON', ['credit'])
    badPoints = rules.rules[0].data['BAD']['basis_points']
    newRate = self.genericProduct.interest_rate + badPoints

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(newRate, self.rules_engine.product.interest_rate)

  def testRulesImportThresholdCreditCheck(self):
    """
    test threshold credit against RulesEngine since Rule should be
    >= threshold gets an interest rate deduction
    """
    rules = RulesImport('JSON', ['credit'])
    goodPoints = rules.rules[0].data['GOOD']['basis_points']
    goodScore = rules.rules[0].data['GOOD']['score']
    newRate = self.genericProduct.interest_rate - goodPoints

    person = Person(goodScore, 'NEVERLAND')

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(newRate, self.rules_engine.product.interest_rate)

  def testRulesImportExcludedStateCheck(self):
    """
    test excluded state against RulesEngine
    excluded here means, product is not offered in certain states
    """
    rules = RulesImport('JSON', ['states'])
    excluded = rules.rules[0].data['excluded']

    person = Person(800, excluded[0])

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(True, self.rules_engine.product.disqualified)

  def testRulesImportIncludedStateCheck(self):
    """
    test included state against RulesEngine
    included here means product is offered if person does not live in an excluded state
    """
    rules = RulesImport('JSON', ['states'])
    person = Person(800, 'NEVERLAND')

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(False, self.rules_engine.product.disqualified)

  def testRulesImportHighIncomeCheck(self):
    """
    test high income against RulesEngine
    """
    person = Person(800, 'NEVERLAND')
    person.setIncome(True, float('inf'), 0)

    rules = RulesImport('JSON', ['income'])

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(False, self.rules_engine.product.disqualified)

  def testRulesImportLowIncomeCheck(self):
    """
    test low income against RulesEngine
    """
    person = Person(800, 'NEVERLAND')
    person.setIncome(True, 0, 0)
    
    rules = RulesImport('JSON', ['income'])

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(True, self.rules_engine.product.disqualified)

  def testRulesImportThresholdIncomeCheck(self):
    """
    test threshold income against RulesEngine
    """
    rules = RulesImport('JSON', ['income'])
    minimumIncome = rules.rules[0].data['income']['minimum']

    person = Person(800, 'NEVERLAND')
    person.setIncome(True, minimumIncome, 0)

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(False, self.rules_engine.product.disqualified)

  def testRulesImportEmployedCheck(self):
    """
    test employed against RulesEngine
    """
    rules = RulesImport('JSON', ['employment'])

    person = Person(800, 'NEVERLAND')
    person.setIncome(True, float('inf'), 0)

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(False, self.rules_engine.product.disqualified)

  def testRulesImportUnemployedCheck(self):
    """
    test unemployed against RulesEngine
    """
    rules = RulesImport('JSON', ['employment'])
    person = Person(800, 'NEVERLAND')
    person.setIncome(False, float('inf'), 0)

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(True, self.rules_engine.product.disqualified)

  def testRulesImportLowDebtCheck(self):
    """
    test low debt against RulesEngine
    """
    person = Person(800, 'NEVERLAND')
    person.setIncome(True, float('inf'), 0)
    rules = RulesImport('JSON', ['debt'])

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(5.0, self.rules_engine.product.interest_rate)

  def testRulesImportHighDebtCheck(self):
    """
    test high debt against RulesEngine
    """
    person = Person(800, 'NEVERLAND')
    person.setIncome(True, float('inf'), 1)
    rules = RulesImport('JSON', ['debt'])
    threshold = rules.rules[0].data['debt']['threshold']
    basisPoints = rules.rules[0].data['debt']['basis_points']
    newRate = self.genericProduct.interest_rate + basisPoints

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(newRate, self.rules_engine.product.interest_rate)

  def testRulesImportThresholdDebtCheck(self):
    """
    test threshold debt against RulesEngine
    """    
    rules = RulesImport('JSON', ['debt'])
    threshold = rules.rules[0].data['debt']['threshold']
    basisPoints = rules.rules[0].data['debt']['basis_points']
    newRate = self.genericProduct.interest_rate + basisPoints
    person = Person(800, 'NEVERLAND')
    person.setIncome(True, float('inf'), threshold)

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(newRate, self.rules_engine.product.interest_rate)

  def testRulesImportProductNameMatchCheck(self):
    """
    test matching product name against RulesEngine
    """
    rules = RulesImport('JSON', ['products'])
    testProductName = next(iter(rules.rules[0].data))
    testProduct = rules.rules[0].data[testProductName]
    testProductAction = testProduct['action']
    testProductPoints = testProduct['basis_points']

    person = Person(800, 'NEVERLAND')
    product = Product(testProductName, 5.0)
   
    if testProductAction == 'add':
      newRate = product.interest_rate + testProductPoints
    elif testProductAction == 'subtract':
      newRate = product.interest_rate - testProductPoints

    self.rules_engine.runRules(person, product, rules)
    self.assertEqual(newRate, self.rules_engine.product.interest_rate)

  def testRulesImportProductNameNoMatchCheck(self):
    """
    test non matching name against RulesEngine
    """
    person = Person(800, 'NEVERLAND')
    product = Product('TEMP', 5.0)
    rules = RulesImport('JSON', ['products'])

    self.rules_engine.runRules(person, self.genericProduct, rules)
    self.assertEqual(5.0, self.rules_engine.product.interest_rate)