import os
from django.conf import settings

from .rules import Rules

class RulesImport(Rules):

  rules = {}

  def __init__(self, source = 'JSON'):
    self.rules = self._getDefaults()
    
    #instructions mentioned rules source could be from different origins and/or format

    if source == 'JSON':
      self._JSON()
    elif source == 'CSV':
      self._CSV()
    elif source == 'MYSQL':
      self._MYSQL()

  def _JSON(self):
    import json

    for cat in self.categories:
      """
      I could have made the folder/path an env setting
      """
      fileName = os.path.join(settings.BASE_DIR, 'products', 'rules', cat + '.json')
      filePointer = open(fileName)
      self.rules[cat] = json.load(filePointer)

    return self.rules

  def _CSV(self):
    return self.rules

  def _MYSQL(self):
    return self.rules

  def getRules(self, key = ''):
    if not key:
      #no key given, return all rules
      return self.rules
    else:
      try:
        return self.rules[key]
      except:
        #key error
        return None
