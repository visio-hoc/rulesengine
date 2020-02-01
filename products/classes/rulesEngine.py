from .person import Person
from .product import Product
from .rules import Rules

class RulesEngine():

  #will be displayed on view if there was an error
  error_message = '' 

  #logs for what rules were processed/used
  logs = []

  def __init__(self):
    #setup hash to link rules to functions
    self.checksHash = {
      'credit': self._credit,
      'products': self._products,
      'states': self._states,
      'income': self._income,
    }

    self.logs = []
    self.error_message = ""

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

    self.logs.append(f'*** Rules processing -> STARTED ***')
    self.logs.append(f'*** INITIAL Interest Rate is {self.product.interest_rate} ***')

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
        self.error_message = f"No function to process {category} rule."
        return 

    self.logs.append(f'*** Rules processing -> ENDED ***')

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
      self.logs.append(f'Credit check -> GOOD score -> decreased by {goodPoints}')
    elif self.person.credit_score < badScore:
      self.product.interest_rate += badPoints
      self.logs.append(f'Credit check -> BAD score -> increased by {badPoints}')

  def _products(self, rule):
    if self.product.name in rule:
      try:
        specific_rule = rule[self.product.name]
        if specific_rule['action'] == 'add':
          self.product.interest_rate += specific_rule['basis_points']
        elif specific_rule['action'] == 'subtract':
          self.product.interest_rate -= specific_rule['basis_points']

        self.logs.append(f'Product check -> rule FOUND -> {specific_rule["action"]} by {specific_rule["basis_points"]}')
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
      self.logs.append(f'States check -> match FOUND, DISQUALIFIED -> {self.person.state} is excluded')

  def _income(self, rule):
    try:
      minimumIncome = rule['income']['minimum']
      employmentStatusRequired = rule['employment']['status']
      debtToIncome = rule['DTI']['max']
    except:
      self.error_message = "Missing values for income rule."
      return

    #if any of the checks disqualifies person, then return

    if self.person.currentIncome < minimumIncome:
      self.product.disqualified = True
      self.logs.append(f'Income check -> TOO LOW -> Person is disqualified.')
      return

    if employmentStatusRequired and not self.person.currentlyEmployed:
      self.product.disqualified = True
      self.logs.append(f'Employment Status check -> UNEMPLOYED -> Person is disqualified.')
      return

    if self.person.debtToIncome >= debtToIncome:
      self.product.disqualified = True
      self.logs.append(f'DTI check -> TOO HIGH -> Person is disqualified.')
      return

  def run_function(self, rule):
    self.functionToCall(rule)