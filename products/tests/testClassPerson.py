from django.test import TestCase

from ..classes.person import Person

class ProductsClassPersonTest(TestCase):

  def setUp(self):
    self.genericPerson = Person(720, 'Florida')

  def testPersonCreation(self):
    """
    test if Person object was instantiated properly
    """
    self.assertTrue(isinstance(self.genericPerson, Person))

    self.assertEqual(720, self.genericPerson.credit_score)
    self.assertEqual('Florida', self.genericPerson.state)
    self.assertEqual(self.genericPerson.__str__(), f'{self.genericPerson.credit_score}: {self.genericPerson.state}')

  def testPersonMethodSetIncome(self):
    """
    test if setIncome method in Person performs as expected
    """
    self.genericPerson.setIncome(False, 52000, 0.5)

    self.assertEqual(False, self.genericPerson.currentlyEmployed)
    self.assertEqual(52000, self.genericPerson.currentIncome)
    self.assertEqual(0.5, self.genericPerson.debtToIncome)
