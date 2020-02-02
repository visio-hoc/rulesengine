import os
from django.conf import settings

from .rule import Rule

class RulesImport(Rule):

  rules = {}
  source = ""

  def __init__(self, source = 'JSON', categories = []):
    self.source = source

    if categories == []:
      #empty rules categories, get defaults
      self.categories = self._getDefaults()
    else:
      self.categories = categories

    """
    import rules
    instructions mentioned rules source could be from different origins and/or format
    """
    if self.source == 'JSON':
      self._JSON()
    elif self.source == 'CSV':
      self._CSV()
    elif self.source == 'MYSQL':
      self._MYSQL()

  def _JSON(self):
    import json

    for cat in self.categories:
      """
      I could have made the folder/path an env setting
      """
      fileName = os.path.join(settings.BASE_DIR, 'products', 'rules', cat + '.json')
      filePointer = open(fileName)
      self.rules.update({cat: json.load(filePointer)})

    return self.rules

  def _CSV(self):
    return self.rules

  def _MYSQL(self):
    return self.rules
