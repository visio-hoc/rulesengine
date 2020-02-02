from django.test import TestCase

from ..classes.person import Person
from ..classes.product import Product
from ..classes.rulesImport import RulesImport
from ..classes.rulesEngine import RulesEngine

class ProductsClassRulesEngineTest(TestCase):
#['credit', 'products', 'states','income', 'debt', 'employment']
  def setUp(self):
    self.genericProduct = Product('TEMP', 5.0)

  def testRulesImportGoodCreditCheck(self):
    """
    test good credit against RulesEngine
    """
    person = Person(800, 'Texas')

    rules = RulesImport('JSON', ['credit'])
    goodPoints = rules.rules['credit']['GOOD']['basis_points']
    newRate = self.genericProduct.interest_rate - goodPoints

    rules_engine = RulesEngine()
    rules_engine.runRules(person, self.genericProduct, rules)

    self.assertEqual(newRate, rules_engine.product.interest_rate)

  def testRulesImportBadCreditCheck(self):
    """
    test bad credit against RulesEngine
    """
    person = Person(500, 'Texas')
    
    rules = RulesImport('JSON', ['credit'])
    badPoints = rules.rules['credit']['BAD']['basis_points']
    newRate = self.genericProduct.interest_rate + badPoints

    rules_engine = RulesEngine()
    rules_engine.runRules(person, self.genericProduct, rules)

    self.assertEqual(newRate, rules_engine.product.interest_rate)

  def testRulesImportThresholdCreditCheck(self):
    """
    test bad credit against RulesEngine
    """
    rules = RulesImport('JSON', ['credit'])
    goodPoints = rules.rules['credit']['GOOD']['basis_points']
    goodScore = rules.rules['credit']['GOOD']['score']
    newRate = self.genericProduct.interest_rate - goodPoints

    person = Person(goodScore, 'Texas')

    rules_engine = RulesEngine()
    rules_engine.runRules(person, self.genericProduct, rules)

    self.assertEqual(newRate, rules_engine.product.interest_rate)