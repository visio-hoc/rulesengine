from django.urls import reverse
from django.test import TestCase

from ..classes.product import Product

class ProductsClassProductTest(TestCase):

  def setUp(self):
    self.genericProduct = Product('7-1 ARM', 5.0)

  def testProductCreation(self):
    """
    test if Product object was instantiated properly
    """
    self.assertTrue(isinstance(self.genericProduct, Product))

    self.assertEqual("7-1 ARM", self.genericProduct.name)
    self.assertEqual(5.0, self.genericProduct.interest_rate)
    self.assertEqual(self.genericProduct.__str__(), f'{self.genericProduct.name}')
