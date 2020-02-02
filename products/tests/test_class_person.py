from django.urls import reverse
from django.test import TestCase

from ..classes.person import Person

class ProductsClassPersonTest(TestCase):

  def setUp(self):
    self.genericPerson = Person(720, 'Florida')

  def testPersonCreation(self):
    self.assertTrue(isinstance(self.genericPerson, Person))
    self.assertEqual(self.genericPerson.__str__(), f'{self.genericPerson.credit_score}: {self.genericPerson.state}')

  def testPersonIncome(self):
    