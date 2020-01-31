from django.shortcuts import render
from django.http import HttpResponse

from .classes.person import Person
from .classes.product import Product

# Create your views here.
def home(request):
    person = Person(720, 'FL')
    print(person)
    product = Product('7-1 ARM', 5.0)
    print(product)
    
    return HttpResponse('Hello, World!')
