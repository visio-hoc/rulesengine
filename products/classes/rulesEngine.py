from .person import Person
from .product import Product
from .rulesImport import RulesImport
from .logger import Logger

class RulesEngine():

  #will be displayed on view if there was an error
  error_message = ''

  def __init__(self):
    self.logger = Logger()
    self.error_message = ""

  def runRules(self, person: Person, product: Product, rules: RulesImport):    
    if not rules:
      #can't move forward without rules
      self.error_message = "Empty rule set given."
      return 

    self.person = person
    self.originalProduct = product #preserve starting product info
    self.product = Product(product.name, product.interest_rate)
    self.rules = rules.rules

    self.logger.logAdd(f'*** Rules processing -> STARTED ***')
    self.logger.logAdd(f'*** INITIAL Interest Rate is {self.product.interest_rate} ***')

    #run all the rules in self.rules list
    for rule in self.rules:
      rule.processRule(self.person, self.product, self.logger)

    self.logger.logAdd(f'*** FINAL Interest Rate is {self.product.interest_rate} ***')
    self.logger.logAdd(f'*** Rules processing -> ENDED ***')