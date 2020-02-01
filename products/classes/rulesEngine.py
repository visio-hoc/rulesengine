from .person import Person
from .product import Product
from .rules import Rules

class RulesEngine():

  #will be displayed on view if there was an error
  error_message = '' 

  def __init__(self):
    #setup hash to link rules to functions
    self.checksHash = {
      'credit': self._credit,
      'products': self._products,
      'states': self._states,
    }

  def runRules(self, person: Person, product: Product, rules: Rules):    
    if not rules:
      #can't move forward without rules
      self.error_message = "Empty rule set given."
      return 

    self.person = person
    self.product = product
    self.rules = rules

    self.checks = self.rules.getRules().keys()
    self._processRules()

  def _processRules(self):
    """
    This function calls check functions dynamically based on the keys in
    the rules property
    """   

    for category in self.checks:
      try:
        rule = self.rules.getRules(category)
      except:
        self.error_message = f"No {category} rule found."
        return

      try:
        self.functionToCall = self.checksHash[category]
        self.run_function(rule)
      except:
        self.error_message = "No function to process rule."
        return 

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
    elif self.person.credit_score < badScore:
      self.product.interest_rate += badPoints

  def _products(self, rule):
    if self.product.name in rule:
      try:
        specific_rule = rule[self.product.name]
        if specific_rule['action'] == 'add':
          self.product.interest_rate += specific_rule['basis_points']
        elif specific_rule['action'] == 'subtract':
          self.product.interest_rate -= specific_rule['basis_points']
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

  def run_function(self, rule):
    self.functionToCall(rule)
