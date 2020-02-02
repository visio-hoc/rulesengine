from .person import Person
from .product import Product
from .rule import Rule
from .logger import Logger

class RulesEngine(Logger):

  #will be displayed on view if there was an error
  error_message = ''

  def __init__(self):
    #setup dict to link rules to functions
    self.checksHash = {
      'credit': self._credit,
      'products': self._products,
      'states': self._states,
      'income': self._income,
      'debt': self._debt,
      'employment': self._employment,
    }

    self.logs = []
    self.error_message = ""

  def runRules(self, person: Person, product: Product, rules: Rule):    
    if not rules:
      #can't move forward without rules
      self.error_message = "Empty rule set given."
      return 

    self.person = person
    self.originalProduct = product
    self.product = Product(product.name, product.interest_rate)
    self.rules = rules.rules

    #get all rule categories (credit, state, etc.) that were loaded
    self.checks = self.rules.keys()
    self._processRules()

  def _processRules(self):
    """
    This function calls check functions (_credit, _state, etc.) dynamically 
    based on the keys (credit, state, etc.) in the rules property 
    """   

    self.logAdd(f'*** Rules processing -> STARTED ***')
    self.logAdd(f'*** INITIAL Interest Rate is {self.product.interest_rate} ***')

    for category in self.checks:
      try:
        rule = self.rules[category]
      except:
        self.error_message = f"No {category} rule found."
        return
        
      try:
        """
        Python doesn't have a native way to use variables as function names,
        so you have to store reference to function then call it.
        """
        self.functionToCall = self.checksHash[category]
        self.run_function(rule)
      except:
        self.error_message = f"No function to process {category} rule."
        return 

    self.logAdd(f'*** FINAL Interest Rate is {self.product.interest_rate} ***')
    self.logAdd(f'*** Rules processing -> ENDED ***')

  def _credit(self, rule):    
    try:
      goodScore = rule['GOOD']['score']
      goodPoints = rule['GOOD']['basis_points']
      badScore = rule['BAD']['score']
      badPoints = rule['BAD']['basis_points']
    except:
      self.error_message = "Missing values for credit score rule."
      return

    if self.person.credit_score >= goodScore:
      self.product.interest_rate -= goodPoints
      self.logAdd(f'Credit check -> GOOD score -> decreased rate by {goodPoints}')
    elif self.person.credit_score < badScore:
      self.product.interest_rate += badPoints
      self.logAdd(f'Credit check -> BAD score -> increased rate by {badPoints}')

  def _products(self, rule):
    if self.product.name in rule:
      try:
        specific_rule = rule[self.product.name]
        if specific_rule['action'] == 'add':
          self.product.interest_rate += specific_rule['basis_points']
        elif specific_rule['action'] == 'subtract':
          self.product.interest_rate -= specific_rule['basis_points']

        self.logAdd(f'Product check -> rule FOUND -> {specific_rule["action"]} by {specific_rule["basis_points"]}')
      except:
        self.error_message = "Missing values for credit score rule."

  def _states(self, rule):
    try:
      excluded = rule['excluded']
    except:
      self.error_message = "Missing values for products rule."
      return

    if self.person.state in excluded:
      self.product.disqualified = True
      self.logAdd(f'States check -> match FOUND, DISQUALIFIED -> {self.person.state} is excluded')

  def _income(self, rule):
    try:
      minimumIncome = rule['income']['minimum']
    except:
      self.error_message = "Missing values for income rule."
      return

    if self.person.currentIncome < minimumIncome:
      self.product.disqualified = True
      self.logAdd(f'Income check -> TOO LOW -> Person is disqualified.')

  def _debt(self, rule):
    try:
      threshold = rule['debt']['threshold']
      basis_points = rule['debt']['basis_points']
    except:
      self.error_message = "Missing values for debt rule."
      return

    if self.person.debtToIncome >= threshold:
      self.product.interest_rate += basis_points
      self.logAdd(f'Debt check -> threshold REACHED -> increase rate by {basis_points}')

  def _employment(self, rule):
    try:
      employmentStatusRequired = rule['employment']['required']
    except:
      self.error_message = "Missing values for employment rule."
      return

    if employmentStatusRequired and not self.person.currentlyEmployed:
      self.product.disqualified = True
      self.logAdd(f'Employment Status check -> UNEMPLOYED -> Person is disqualified.')

  def run_function(self, rule):
    #calls method reference
    self.functionToCall(rule)