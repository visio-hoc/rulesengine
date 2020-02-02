from django.urls import reverse
from django.test import TestCase

from ..classes.person import Person
from ..classes.product import Product
from ..classes.rulesEngine import RulesEngine

class ProductsViewsTest(TestCase):

  def setUp(self):
    pass

  def test_home_view_meta(self):
    """
    test if home view response is proper
    """

    url = reverse("product-home")
    resp = self.client.get(url)

    #page loads properly
    self.assertEqual(resp.status_code, 200)

    #context vars exist and not none
    self.assertIsNotNone(resp.context['data'])
    self.assertIsNotNone(resp.context['logs'])
    self.assertIsNotNone(resp.context['person'])
    self.assertIsNotNone(resp.context['product'])

    #vars are properly typed
    self.assertIsInstance(resp.context['data'], RulesEngine)
    self.assertIsInstance(resp.context['person'], Person)
    self.assertIsInstance(resp.context['product'], Product)
    self.assertIsInstance(resp.context['logs'], list)


  def test_extended_view_meta(self):
    """
    test if extended view response is proper
    """

    url = reverse("product-extended")
    resp = self.client.get(url)

    #page loads properly
    self.assertEqual(resp.status_code, 200)

    #context vars exist and not none
    self.assertIsNotNone(resp.context['data'])
    self.assertIsNotNone(resp.context['logs'])
    self.assertIsNotNone(resp.context['person'])
    self.assertIsNotNone(resp.context['product'])

    #vars are properly typed
    self.assertIsInstance(resp.context['data'], RulesEngine)
    self.assertIsInstance(resp.context['person'], Person)
    self.assertIsInstance(resp.context['product'], Product)
    self.assertIsInstance(resp.context['logs'], list)
