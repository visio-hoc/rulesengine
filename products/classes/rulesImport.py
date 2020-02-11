import os
from django.conf import settings

from .rule import *

"""
import from source class

"""
class RulesImport():

  def __init__(self, source = 'JSON', categories = None):
    #would normally place default categories in app settings
    if categories is None:
      categories = ['credit', 'products', 'states']

    #dict to link data source to class methods
    self.sourceHash = {
      'JSON': self._JSON,
      'CSV': self._CSV,
      'MYSQL': self._MYSQL,
    }

    #initial values
    self.rules = []
    self.source = source
    self.categories = categories

    #set source function
    source = self.sourceHash[source]

    #import rules    
    for category in self.categories:
      #build class name str using the convention of CategoryRule for category rules class
      className = category[0].upper() + category[1:] + 'Rule'
      #save reference to categoryRule class from global vars dict
      classCategory = globals()[className]
      #load data from source based on category
      data = source(category)
      #instantiate and append the new rule class to self.rules
      self.rules.append(classCategory(category, data))

  def _JSON(self, category):
    import json
    """
    I could have made the folder/path an env setting
    """
    fileName = os.path.join(settings.BASE_DIR, 'products', 'rules', category + '.json')
    filePointer = open(fileName)
    return json.load(filePointer)

  def _CSV(self, category):
    pass

  def _MYSQL(self, category):
    pass
