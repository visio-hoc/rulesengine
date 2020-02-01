from django.shortcuts import render

from .classes.person import Person
from .classes.product import Product
from .classes.rulesEngine import RulesEngine
from .classes.rulesImport import RulesImport

# Create your views here.
def home(request):
  person = Person(720, 'Florida')
  product = Product('7-1 ARM', 5.0)
  rules_engine = RulesEngine()
  rules = _loadRules()
  rules_engine.runRules(person, product, rules)
  
  context = {
    'data': rules_engine,
    'logs': rules_engine.logs,
    'person': person,
    'product': product,
  }
  return render(request, 'home.html', context)

def extended(request):
  person = Person(720, 'FL')
  person.setIncome(True, 52000, 0.5)
  product = Product('7-1 ARM', 5.0)
  rules_engine = RulesEngine()

  #using defaults + income rule set
  rules = _loadRules(['credit', 'products', 'states','income'])

  rules_engine.runRules(person, product, rules)
  
  context = {
    'data': rules_engine,
    'logs': rules_engine.logs,
    'person': person,
    'product': product,
  }
  return render(request, 'extended.html', context)

def _loadRules(categories = []):
  """
  I would have prefered to autoload the rules as part of the constructor for 
  RulesEngine or at least made it a method of the RulesEngine class. But in the
  example given, it is a seperate function.

  :type categories: List
  :rtype: Rules
  """
  rules = RulesImport('JSON', categories)
  return rules

