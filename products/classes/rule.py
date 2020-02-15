class Rule():
  """
  Base class for rules object
  """

  def __init__(self, name, data):
    self.name = name
    self.data = data
    self.error_message = ''

  def processRule(self, person, product, logs):
    """
    Method to process rules. Intended to be overridden by children class
    """
    pass

class CreditRule(Rule):
  def processRule(self, person, product, logs):
    try:
      goodScore = self.data['GOOD']['score']
      goodPoints = self.data['GOOD']['basis_points']
      badScore = self.data['BAD']['score']
      badPoints = self.data['BAD']['basis_points']
    except KeyError:
      self.error_message = "Missing values for credit score rule."
      return

    if person.credit_score >= goodScore:
      product.interest_rate -= goodPoints
      logs.logAdd(f'Credit check -> GOOD score -> decreased rate by {goodPoints}')
    elif person.credit_score < badScore:
      product.interest_rate += badPoints
      logs.logAdd(f'Credit check -> BAD score -> increased rate by {badPoints}')

class ProductsRule(Rule):
  def processRule(self, person, product, logs):
    if product.name in self.data:
      try:
        specific_rule = self.data[product.name]
        if specific_rule['action'] == 'add':
          product.interest_rate += specific_rule['basis_points']
        elif specific_rule['action'] == 'subtract':
          product.interest_rate -= specific_rule['basis_points']

        logs.logAdd(f'Product check -> rule FOUND -> {specific_rule["action"]} by {specific_rule["basis_points"]}')
      except KeyError:
        self.error_message = "Missing values for credit score rule."

class StatesRule(Rule):
  def processRule(self, person, product, logs):
    try:
      excluded = self.data['excluded']
    except KeyError:
      self.error_message = "Missing values for products rule."
      return

    if person.state in excluded:
      product.disqualified = True
      logs.logAdd(f'States check -> match FOUND, DISQUALIFIED -> {person.state} is excluded')

class IncomeRule(Rule):
  def processRule(self, person, product, logs):
    try:
      minimumIncome = self.data['income']['minimum']
    except KeyError:
      self.error_message = "Missing values for income rule."
      return

    if person.currentIncome < minimumIncome:
      product.disqualified = True
      logs.logAdd(f'Income check -> TOO LOW -> Person is disqualified.')

class DebtRule(Rule):
  def processRule(self, person, product, logs):
    try:
      threshold = self.data['debt']['threshold']
      basis_points = self.data['debt']['basis_points']
    except KeyError:
      self.error_message = "Missing values for debt rule."
      return

    if person.debtToIncome >= threshold:
      product.interest_rate += basis_points
      logs.logAdd(f'Debt check -> threshold REACHED -> increase rate by {basis_points}')

class EmploymentRule(Rule):
  def processRule(self, person, product, logs):
    try:
      employmentStatusRequired = self.data['employment']['required']
    except KeyError:
      self.error_message = "Missing values for employment rule."
      return

    if employmentStatusRequired and not person.currentlyEmployed:
      product.disqualified = True
      logs.logAdd(f'Employment Status check -> UNEMPLOYED -> Person is disqualified.')