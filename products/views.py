from django.shortcuts import render

from .classes.person import Person
from .classes.product import Product
from .classes.rulesEngine import RulesEngine
from .classes.rulesImport import RulesImport

# Create your views here.
def home(request):
  person = Person(720, 'FL')
  product = Product('7-1 ARM', 5.0)
  rules_engine = RulesEngine()
  rules = _loadRules()
  rules_engine.runRules(person, product, rules)
  
  context = {
    'data': rules_engine,
    'person': person,
    'product': product,
  }
  return render(request, 'home.html', context)

def _loadRules():
  """
  I would have prefered to autoload the rules as part of the constructor for 
  RulesEngine or at least made it a method of the RulesEngine class. But in the
  example given, it is a seperate function.
  """
  rules = RulesImport('JSON')
  return rules

