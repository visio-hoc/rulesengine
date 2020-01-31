from django.shortcuts import render
from django.http import HttpResponse

from .classes.person import Person
from .classes.product import Product
from .classes.rulesEngine import RulesEngine
from .classes.rulesImport import RulesImport

# Create your views here.
def home(request):
    person = Person(720, 'FL')
    print(person)
    product = Product('7-1 ARM', 5.0)
    print(product)

    rules_engine = RulesEngine()
    print(rules_engine)

    rules = _loadRules()
    print(rules.rules)

    return HttpResponse('Hello, World!')

def _loadRules():
  """
  I would have prefered to autoload the rules as part of the constructor for 
  RulesEngine or at least made it a method of the RulesEngine class. But in the
  example given, it a seperate function.
  """
  rules = RulesImport('JSON')
  return rules

